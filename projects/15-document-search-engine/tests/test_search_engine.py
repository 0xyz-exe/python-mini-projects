"""Tests for document search engine."""
from pathlib import Path
from tempfile import TemporaryDirectory
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from search_engine import DocumentSearchEngine


def test_tokenize():
    engine = DocumentSearchEngine(Path("test.json"))
    tokens = engine.tokenize("Hello World! This is a test.")
    assert "hello" in tokens
    assert "world" in tokens
    assert "test" in tokens


def test_index_and_search():
    with TemporaryDirectory() as tmpdir:
        index_path = Path(tmpdir) / "index.json"
        docs_dir = Path(tmpdir) / "docs"
        docs_dir.mkdir()
        
        (docs_dir / "doc1.txt").write_text("Python programming language")
        (docs_dir / "doc2.txt").write_text("JavaScript web development")
        (docs_dir / "doc3.txt").write_text("Python data science")
        
        engine = DocumentSearchEngine(index_path)
        engine.index_directory(docs_dir)
        
        results = engine.search("python")
        assert len(results) == 2
        
        results = engine.search("javascript")
        assert len(results) == 1


def test_persistence():
    with TemporaryDirectory() as tmpdir:
        index_path = Path(tmpdir) / "index.json"
        docs_dir = Path(tmpdir) / "docs"
        docs_dir.mkdir()
        
        (docs_dir / "doc.txt").write_text("test document")
        
        engine1 = DocumentSearchEngine(index_path)
        engine1.index_directory(docs_dir)
        
        engine2 = DocumentSearchEngine(index_path)
        results = engine2.search("test")
        assert len(results) == 1


if __name__ == "__main__":
    test_tokenize()
    test_index_and_search()
    test_persistence()
    print("✓ All tests passed")
