"""Tests for CSV analyzer."""
from pathlib import Path
from tempfile import TemporaryDirectory
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from csv_analyzer import CSVAnalyzer


def test_load_and_summary():
    with TemporaryDirectory() as tmpdir:
        csv_file = Path(tmpdir) / "data.csv"
        csv_file.write_text("name,age,city\nAlice,30,NYC\nBob,25,LA\n")
        
        analyzer = CSVAnalyzer(csv_file)
        analyzer.load()
        
        summary = analyzer.summary()
        assert summary['rows'] == 2
        assert summary['columns'] == 3


def test_missing_values():
    with TemporaryDirectory() as tmpdir:
        csv_file = Path(tmpdir) / "data.csv"
        csv_file.write_text("name,age\nAlice,30\nBob,\nCharlie,25\n")
        
        analyzer = CSVAnalyzer(csv_file)
        analyzer.load()
        
        missing = analyzer.missing_values()
        assert missing.get('age', 0) == 1


def test_numeric_stats():
    with TemporaryDirectory() as tmpdir:
        csv_file = Path(tmpdir) / "data.csv"
        csv_file.write_text("value\n10\n20\n30\n")
        
        analyzer = CSVAnalyzer(csv_file)
        analyzer.load()
        
        stats = analyzer.numeric_stats('value')
        assert stats['min'] == 10.0
        assert stats['max'] == 30.0
        assert stats['mean'] == 20.0


def test_group_by():
    with TemporaryDirectory() as tmpdir:
        csv_file = Path(tmpdir) / "data.csv"
        csv_file.write_text("category,value\nA,10\nB,20\nA,15\n")
        
        analyzer = CSVAnalyzer(csv_file)
        analyzer.load()
        
        groups = analyzer.group_by('category')
        assert groups['A'] == 2
        assert groups['B'] == 1


if __name__ == "__main__":
    test_load_and_summary()
    test_missing_values()
    test_numeric_stats()
    test_group_by()
    print("✓ All tests passed")
