"""Tests for text analyzer."""
from pathlib import Path
from tempfile import TemporaryDirectory
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from text_analyzer import TextAnalyzer


def test_count_stats():
    with TemporaryDirectory() as tmpdir:
        file_path = Path(tmpdir) / "test.txt"
        file_path.write_text("Hello world\nThis is a test\n\nAnother line")
        
        analyzer = TextAnalyzer(file_path)
        stats = analyzer.count_stats()
        
        assert stats['lines'] == 4
        assert stats['words'] == 8  # Hello world This is a test Another line
        assert stats['non_empty_lines'] == 3


def test_frequent_words():
    with TemporaryDirectory() as tmpdir:
        file_path = Path(tmpdir) / "test.txt"
        file_path.write_text("test test test word word other")
        
        analyzer = TextAnalyzer(file_path)
        freq = analyzer.frequent_words(top_n=2)
        
        assert freq[0] == ('test', 3)
        assert freq[1] == ('word', 2)


def test_analyze_logs():
    with TemporaryDirectory() as tmpdir:
        file_path = Path(tmpdir) / "app.log"
        file_path.write_text(
            "2026-10-18 ERROR: Connection failed\n"
            "2026-10-18 INFO: Starting service\n"
            "2026-10-18 ERROR: Timeout\n"
        )
        
        analyzer = TextAnalyzer(file_path)
        levels = analyzer.analyze_logs()
        
        assert levels['ERROR'] == 2
        assert levels['INFO'] == 1


def test_filter_logs():
    with TemporaryDirectory() as tmpdir:
        file_path = Path(tmpdir) / "app.log"
        file_path.write_text(
            "2026-10-18 ERROR: Database error\n"
            "2026-10-18 INFO: Request processed\n"
            "2026-10-19 ERROR: Another error\n"
        )
        
        analyzer = TextAnalyzer(file_path)
        
        errors = analyzer.filter_logs(keyword="ERROR")
        assert len(errors) == 2
        
        date_filtered = analyzer.filter_logs(date_prefix="2026-10-18")
        assert len(date_filtered) == 2


if __name__ == "__main__":
    test_count_stats()
    test_frequent_words()
    test_analyze_logs()
    test_filter_logs()
    print("✓ All tests passed")
