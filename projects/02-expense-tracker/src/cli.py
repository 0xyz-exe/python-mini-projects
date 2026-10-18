#!/usr/bin/env python3
"""Expense Tracker - CLI."""
import argparse
from pathlib import Path
from expense_tracker import ExpenseTracker


def main():
    parser = argparse.ArgumentParser(description="Expense Tracker")
    parser.add_argument("--storage", default="expenses.json", help="Storage file")
    
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # Add
    add = subparsers.add_parser("add", help="Add transaction")
    add.add_argument("type", choices=["income", "expense"])
    add.add_argument("amount", type=float)
    add.add_argument("category")
    add.add_argument("-d", "--description", default="")
    add.add_argument("--date", help="YYYY-MM-DD format")
    
    # Delete
    delete = subparsers.add_parser("delete", help="Delete transaction")
    delete.add_argument("id", type=int)
    
    # List
    list_parser = subparsers.add_parser("list", help="List transactions")
    
    # Monthly summary
    month = subparsers.add_parser("monthly", help="Monthly summary")
    month.add_argument("year", type=int)
    month.add_argument("month", type=int)
    
    # Category summary
    subparsers.add_parser("categories", help="Category breakdown")
    
    # Export
    export = subparsers.add_parser("export", help="Export to CSV")
    export.add_argument("path")
    
    # Import
    import_parser = subparsers.add_parser("import", help="Import from CSV")
    import_parser.add_argument("path")
    
    args = parser.parse_args()
    
    try:
        et = ExpenseTracker(Path(args.storage))
        
        if args.command == "add":
            txn = et.add(args.type, args.amount, args.category, args.description, args.date)
            print(f"✓ Added {txn.type} #{txn.id}: ${txn.amount:.2f} - {txn.category}")
        
        elif args.command == "delete":
            et.delete(args.id)
            print(f"✓ Deleted transaction #{args.id}")
        
        elif args.command == "list":
            for txn in et.transactions:
                sign = "+" if txn.type == "income" else "-"
                print(f"#{txn.id} {txn.date} {sign}${txn.amount:.2f} [{txn.category}] {txn.description}")
        
        elif args.command == "monthly":
            summary = et.monthly_summary(args.year, args.month)
            print(f"Month: {summary['month']}")
            print(f"Income:  ${summary['income']:.2f}")
            print(f"Expense: ${summary['expense']:.2f}")
            print(f"Balance: ${summary['balance']:.2f}")
            print(f"Transactions: {summary['count']}")
        
        elif args.command == "categories":
            categories = et.category_summary()
            for key, amount in sorted(categories.items(), key=lambda x: -x[1]):
                print(f"{key}: ${amount:.2f}")
        
        elif args.command == "export":
            et.export_csv(Path(args.path))
            print(f"✓ Exported to {args.path}")
        
        elif args.command == "import":
            et.import_csv(Path(args.path))
            print(f"✓ Imported from {args.path}")
    
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
