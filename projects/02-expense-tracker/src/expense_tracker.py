"""Expense Tracker - Core functionality."""
import json
import csv
from datetime import datetime
from pathlib import Path
from typing import List, Optional
from dataclasses import dataclass, asdict


@dataclass
class Transaction:
    """Transaction representation."""
    id: int
    type: str  # "income" or "expense"
    amount: float
    category: str
    description: str
    date: str
    
    def __post_init__(self):
        if self.type not in ["income", "expense"]:
            raise ValueError("Type must be 'income' or 'expense'")
        if self.amount <= 0:
            raise ValueError("Amount must be positive")


class ExpenseTracker:
    """Manage income and expenses with persistence."""
    
    def __init__(self, storage_path: Path):
        self.storage_path = storage_path
        self.transactions: List[Transaction] = []
        self.load()
    
    def load(self):
        """Load transactions from JSON."""
        if self.storage_path.exists():
            with open(self.storage_path) as f:
                data = json.load(f)
                self.transactions = [Transaction(**t) for t in data]
    
    def save(self):
        """Save transactions to JSON."""
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.storage_path, 'w') as f:
            json.dump([asdict(t) for t in self.transactions], f, indent=2)
    
    def add(self, type_: str, amount: float, category: str, 
            description: str = "", date: Optional[str] = None) -> Transaction:
        """Add transaction."""
        if not category.strip():
            raise ValueError("Category cannot be empty")
        
        txn_id = max([t.id for t in self.transactions], default=0) + 1
        txn_date = date or datetime.now().strftime("%Y-%m-%d")
        txn = Transaction(txn_id, type_, amount, category, description, txn_date)
        self.transactions.append(txn)
        self.save()
        return txn
    
    def delete(self, txn_id: int):
        """Delete transaction."""
        txn = self._find(txn_id)
        self.transactions.remove(txn)
        self.save()
    
    def monthly_summary(self, year: int, month: int) -> dict:
        """Get monthly income/expense summary."""
        month_str = f"{year:04d}-{month:02d}"
        monthly = [t for t in self.transactions if t.date.startswith(month_str)]
        
        income = sum(t.amount for t in monthly if t.type == "income")
        expense = sum(t.amount for t in monthly if t.type == "expense")
        
        return {
            "month": month_str,
            "income": income,
            "expense": expense,
            "balance": income - expense,
            "count": len(monthly)
        }
    
    def category_summary(self) -> dict:
        """Get breakdown by category."""
        categories = {}
        for txn in self.transactions:
            key = f"{txn.type}:{txn.category}"
            categories[key] = categories.get(key, 0) + txn.amount
        return categories
    
    def export_csv(self, path: Path):
        """Export to CSV."""
        with open(path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'type', 'amount', 'category', 'description', 'date'])
            writer.writeheader()
            for txn in self.transactions:
                writer.writerow(asdict(txn))
    
    def import_csv(self, path: Path):
        """Import from CSV."""
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Avoid ID collision
                max_id = max([t.id for t in self.transactions], default=0)
                row['id'] = max_id + 1
                row['amount'] = float(row['amount'])
                self.transactions.append(Transaction(**row))
        self.save()
    
    def _find(self, txn_id: int) -> Transaction:
        """Find transaction by ID."""
        for txn in self.transactions:
            if txn.id == txn_id:
                return txn
        raise ValueError(f"Transaction {txn_id} not found")
