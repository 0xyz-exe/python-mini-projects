"""Tests for batch file renamer."""
from pathlib import Path
from tempfile import TemporaryDirectory
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from file_renamer import FileRenamer


def test_add_prefix():
    with TemporaryDirectory() as tmpdir:
        dir_path = Path(tmpdir)
        (dir_path / "file1.txt").touch()
        (dir_path / "file2.txt").touch()
        
        renamer = FileRenamer(dir_path)
        ops = renamer.add_prefix("new_")
        
        assert len(ops) == 2
        assert any("new_file1.txt" in str(new) for _, new in ops)


def test_add_suffix():
    with TemporaryDirectory() as tmpdir:
        dir_path = Path(tmpdir)
        (dir_path / "file.txt").touch()
        
        renamer = FileRenamer(dir_path)
        ops = renamer.add_suffix("_backup")
        
        assert len(ops) == 1
        assert "file_backup.txt" in str(ops[0][1])


def test_numbering():
    with TemporaryDirectory() as tmpdir:
        dir_path = Path(tmpdir)
        (dir_path / "c.txt").touch()
        (dir_path / "a.txt").touch()
        (dir_path / "b.txt").touch()
        
        renamer = FileRenamer(dir_path)
        ops = renamer.add_numbering(start=1)
        
        assert len(ops) == 3
        names = [new.name for _, new in ops]
        assert "001.txt" in names
        assert "003.txt" in names


def test_find_replace():
    with TemporaryDirectory() as tmpdir:
        dir_path = Path(tmpdir)
        (dir_path / "old_file.txt").touch()
        (dir_path / "other.txt").touch()
        
        renamer = FileRenamer(dir_path)
        ops = renamer.find_replace("old", "new")
        
        assert len(ops) == 1
        assert "new_file.txt" in str(ops[0][1])


def test_extension_filter():
    with TemporaryDirectory() as tmpdir:
        dir_path = Path(tmpdir)
        (dir_path / "doc.txt").touch()
        (dir_path / "img.png").touch()
        
        renamer = FileRenamer(dir_path)
        ops = renamer.add_prefix("pre_", extensions=[".txt"])
        
        assert len(ops) == 1
        assert "pre_doc.txt" in str(ops[0][1])


def test_collision_detection():
    with TemporaryDirectory() as tmpdir:
        dir_path = Path(tmpdir)
        (dir_path / "file1.txt").touch()
        (dir_path / "file2.txt").touch()
        (dir_path / "prefix_file1.txt").touch()  # Will collide with prefix operation
        
        renamer = FileRenamer(dir_path)
        ops = renamer.add_prefix("prefix_")
        
        # Verify collision would occur
        assert len(ops) == 3  # file1, file2, prefix_file1
        
        try:
            renamer.execute(dry_run=False)
            assert False, "Should detect collision"
        except ValueError as e:
            assert "collision" in str(e).lower()


def test_execute_real():
    with TemporaryDirectory() as tmpdir:
        dir_path = Path(tmpdir)
        file1 = dir_path / "original.txt"
        file1.touch()
        
        renamer = FileRenamer(dir_path)
        renamer.add_prefix("renamed_")
        log = renamer.execute(dry_run=False)
        
        assert len(log) == 1
        assert (dir_path / "renamed_original.txt").exists()
        assert not file1.exists()


if __name__ == "__main__":
    test_add_prefix()
    test_add_suffix()
    test_numbering()
    test_find_replace()
    test_extension_filter()
    test_collision_detection()
    test_execute_real()
    print("✓ All tests passed")
