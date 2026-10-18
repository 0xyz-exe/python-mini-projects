"""Text and Log Analyzer - Core functionality."""
from pathlib import Path
from typing import Dict, List
from collections import Counter
import re


class TextAnalyzer:
    """Analyze text files and logs."""
    
    def __init__(self, file_path: Path):
        self.file_path = Path(file_path)
    
    def count_stats(self) -> Dict[str, int]:
        """Count basic text statistics."""
        if not self.file_path.exists():
            raise ValueError(f"File not found: {self.file_path}")
        
        with open(self.file_path, encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        words = re.findall(r'\w+', content)
        lines = content.split('\n')
        
        return {
            'characters': len(content),
            'words': len(words),
            'lines': len(lines),
            'non_empty_lines': len([l for l in lines if l.strip()])
        }
    
    def frequent_words(self, top_n: int = 10, min_length: int = 3) -> List[tuple]:
        """Get most frequent words."""
        with open(self.file_path, encoding='utf-8', errors='ignore') as f:
            content = f.read().lower()
        
        words = re.findall(r'\w+', content)
        words = [w for w in words if len(w) >= min_length]
        
        counter = Counter(words)
        return counter.most_common(top_n)
    
    def analyze_logs(self, levels: List[str] = None) -> Dict[str, int]:
        """Analyze log severity levels."""
        if levels is None:
            levels = ['ERROR', 'WARN', 'WARNING', 'INFO', 'DEBUG']
        
        counts = {level: 0 for level in levels}
        
        with open(self.file_path, encoding='utf-8', errors='ignore') as f:
            for line in f:
                line_upper = line.upper()
                for level in levels:
                    if level in line_upper:
                        counts[level] += 1
                        break
        
        return counts
    
    def filter_logs(self, keyword: str = None, date_prefix: str = None) -> List[str]:
        """Filter log entries by keyword or date."""
        results = []
        
        with open(self.file_path, encoding='utf-8', errors='ignore') as f:
            for line in f:
                include = True
                
                if keyword and keyword.lower() not in line.lower():
                    include = False
                
                if date_prefix and not line.startswith(date_prefix):
                    include = False
                
                if include:
                    results.append(line.rstrip())
        
        return results
    
    def export_report(self, output_path: Path, format: str = 'json'):
        """Export analysis report."""
        import json
        import csv
        
        stats = self.count_stats()
        freq = self.frequent_words()
        
        if format == 'json':
            report = {
                'file': str(self.file_path),
                'statistics': stats,
                'frequent_words': [{'word': w, 'count': c} for w, c in freq]
            }
            with open(output_path, 'w') as f:
                json.dump(report, f, indent=2)
        
        elif format == 'csv':
            with open(output_path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['metric', 'value'])
                for key, val in stats.items():
                    writer.writerow([key, val])
