"""Tests for duplicate file finder."""
from pathlib import Path
from tempfile import TemporaryDirectory
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from duplicate_finder import DuplicateFinder


def test_find_duplicates():
    with TemporaryDirectory() as tmpdir:
        dir_path = Path(tmpdir)
        
        # Create duplicates
        (dir_path / "file1.txt").write_text("content")
        (dir_path / "file2.txt").write_text("content")
        (dir_path / "unique.txt").write_text("unique")
        
        finder = DuplicateFinder(dir_path)
        duplicates = finder.find_duplicates()
        
        assert len(duplicates) == 1
        assert any(len(files) == 2 for files in duplicates.values())


def test_no_duplicates():
    with TemporaryDirectory() as tmpdir:
        dir_path = Path(tmpdir)
        
        (dir_path / "file1.txt").write_text("content1")
        (dir_path / "file2.txt").write_text("content2")
        
        finder = DuplicateFinder(dir_path)
        duplicates = finder.find_duplicates()
        
        assert len(duplicates) == 0


def test_min_size_filter():
    with TemporaryDirectory() as tmpdir:
        dir_path = Path(tmpdir)
        
        (dir_path / "small1.txt").write_text("x")
        (dir_path / "small2.txt").write_text("x")
        
        finder = DuplicateFinder(dir_path)
        duplicates = finder.find_duplicates(min_size=10)
        
        assert len(duplicates) == 0


def test_summary():
    with TemporaryDirectory() as tmpdir:
        dir_path = Path(tmpdir)
        
        (dir_path / "dup1.txt").write_text("content")
        (dir_path / "dup2.txt").write_text("content")
        (dir_path / "dup3.txt").write_text("content")
        
        finder = DuplicateFinder(dir_path)
        finder.find_duplicates()
        summary = finder.get_summary()
        
        assert summary['duplicate_groups'] == 1
        assert summary['total_duplicate_files'] == 3


if __name__ == "__main__":
    test_find_duplicates()
    test_no_duplicates()
    test_min_size_filter()
    test_summary()
    print("✓ All tests passed")
