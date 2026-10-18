"""CSV Data Analyzer."""
import csv
from pathlib import Path
from typing import Dict, List, Any
from collections import defaultdict


class CSVAnalyzer:
    """Analyze CSV data."""
    
    def __init__(self, csv_path: Path):
        self.csv_path = Path(csv_path)
        self.data: List[Dict[str, Any]] = []
        self.headers: List[str] = []
    
    def load(self):
        """Load CSV file."""
        with open(self.csv_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            self.headers = reader.fieldnames or []
            self.data = list(reader)
    
    def summary(self) -> Dict:
        """Get basic summary."""
        return {
            'rows': len(self.data),
            'columns': len(self.headers),
            'headers': self.headers
        }
    
    def missing_values(self) -> Dict[str, int]:
        """Count missing values per column."""
        missing = defaultdict(int)
        for row in self.data:
            for col in self.headers:
                if not row.get(col, '').strip():
                    missing[col] += 1
        return dict(missing)
    
    def numeric_stats(self, column: str) -> Dict:
        """Get numeric statistics for column."""
        values = []
        for row in self.data:
            try:
                val = float(row.get(column, ''))
                values.append(val)
            except ValueError:
                continue
        
        if not values:
            return {'error': 'No numeric values found'}
        
        values.sort()
        n = len(values)
        
        return {
            'count': n,
            'min': values[0],
            'max': values[-1],
            'mean': sum(values) / n,
            'median': values[n // 2] if n % 2 else (values[n // 2 - 1] + values[n // 2]) / 2
        }
    
    def group_by(self, column: str) -> Dict[str, int]:
        """Group by column and count."""
        groups = defaultdict(int)
        for row in self.data:
            key = row.get(column, 'N/A')
            groups[key] += 1
        return dict(groups)
    
    def export_cleaned(self, output_path: Path, drop_empty_rows: bool = False):
        """Export cleaned data."""
        cleaned = self.data
        if drop_empty_rows:
            cleaned = [row for row in self.data if any(v.strip() for v in row.values())]
        
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=self.headers)
            writer.writeheader()
            writer.writerows(cleaned)
