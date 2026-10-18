"""Tests for file organizer."""
from pathlib import Path
from tempfile import TemporaryDirectory
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from file_organizer import FileOrganizer


def test_organize_by_extension_dry_run():
    with TemporaryDirectory() as tmpdir:
        source = Path(tmpdir) / "source"
        dest = Path(tmpdir) / "dest"
        source.mkdir()
        
        (source / "doc.txt").touch()
        (source / "image.png").touch()
        (source / "script.py").touch()
        
        organizer = FileOrganizer(source, dest)
        result = organizer.organize_by_extension(dry_run=True)
        
        assert ".txt" in result
        assert ".png" in result
        assert ".py" in result
        assert not dest.exists()  # Dry run doesn't create


def test_organize_by_extension_real():
    with TemporaryDirectory() as tmpdir:
        source = Path(tmpdir) / "source"
        dest = Path(tmpdir) / "dest"
        source.mkdir()
        
        (source / "doc.txt").write_text("content")
        (source / "image.png").write_text("image")
        
        organizer = FileOrganizer(source, dest)
        result = organizer.organize_by_extension(dry_run=False)
        
        assert (dest / "txt" / "doc.txt").exists()
        assert (dest / "png" / "image.png").exists()
        assert len(organizer.get_log()) == 2


def test_organize_by_type():
    with TemporaryDirectory() as tmpdir:
        source = Path(tmpdir) / "source"
        dest = Path(tmpdir) / "dest"
        source.mkdir()
        
        (source / "doc.pdf").touch()
        (source / "pic.jpg").touch()
        (source / "code.py").touch()
        (source / "video.mp4").touch()
        
        organizer = FileOrganizer(source, dest)
        result = organizer.organize_by_type(dry_run=True)
        
        assert "documents" in result
        assert "images" in result
        assert "code" in result
        assert "videos" in result


def test_collision_handling():
    with TemporaryDirectory() as tmpdir:
        source = Path(tmpdir) / "source"
        dest = Path(tmpdir) / "dest"
        source.mkdir()
        dest.mkdir()
        
        (source / "file.txt").write_text("content1")
        (dest / "txt").mkdir()
        (dest / "txt" / "file.txt").write_text("existing")
        
        organizer = FileOrganizer(source, dest)
        organizer.organize_by_extension(dry_run=False)
        
        assert (dest / "txt" / "file_1.txt").exists()


def test_nonexistent_source():
    with TemporaryDirectory() as tmpdir:
        source = Path(tmpdir) / "nonexistent"
        dest = Path(tmpdir) / "dest"
        
        organizer = FileOrganizer(source, dest)
        try:
            organizer.organize_by_extension()
            assert False
        except ValueError as e:
            assert "does not exist" in str(e)


if __name__ == "__main__":
    test_organize_by_extension_dry_run()
    test_organize_by_extension_real()
    test_organize_by_type()
    test_collision_handling()
    test_nonexistent_source()
    print("✓ All tests passed")
