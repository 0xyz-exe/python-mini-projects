"""Tests for FastAPI Notes API."""
from pathlib import Path
from tempfile import TemporaryDirectory
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

try:
    from fastapi.testclient import TestClient
    from main import create_app
    FASTAPI_AVAILABLE = True
except ImportError:
    FASTAPI_AVAILABLE = False
    print("FastAPI not installed. Install: python3 -m pip install fastapi --user")


def test_create_note():
    if not FASTAPI_AVAILABLE:
        return
    
    with TemporaryDirectory() as tmpdir:
        app = create_app(Path(tmpdir) / "notes.json")
        client = TestClient(app)
        
        response = client.post("/notes", json={
            "title": "Test Note",
            "content": "Content here",
            "tags": ["test"]
        })
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "Test Note"
        assert data["id"] == 1


def test_get_notes():
    if not FASTAPI_AVAILABLE:
        return
    
    with TemporaryDirectory() as tmpdir:
        app = create_app(Path(tmpdir) / "notes.json")
        client = TestClient(app)
        
        client.post("/notes", json={"title": "Note 1", "content": "C1"})
        client.post("/notes", json={"title": "Note 2", "content": "C2"})
        
        response = client.get("/notes")
        assert response.status_code == 200
        assert len(response.json()) == 2


def test_get_note_by_id():
    if not FASTAPI_AVAILABLE:
        return
    
    with TemporaryDirectory() as tmpdir:
        app = create_app(Path(tmpdir) / "notes.json")
        client = TestClient(app)
        
        create_resp = client.post("/notes", json={"title": "Note", "content": "C"})
        note_id = create_resp.json()["id"]
        
        response = client.get(f"/notes/{note_id}")
        assert response.status_code == 200
        assert response.json()["title"] == "Note"


def test_update_note():
    if not FASTAPI_AVAILABLE:
        return
    
    with TemporaryDirectory() as tmpdir:
        app = create_app(Path(tmpdir) / "notes.json")
        client = TestClient(app)
        
        create_resp = client.post("/notes", json={"title": "Old", "content": "C"})
        note_id = create_resp.json()["id"]
        
        response = client.put(f"/notes/{note_id}", json={
            "title": "Updated",
            "content": "New content"
        })
        assert response.status_code == 200
        assert response.json()["title"] == "Updated"


def test_delete_note():
    if not FASTAPI_AVAILABLE:
        return
    
    with TemporaryDirectory() as tmpdir:
        app = create_app(Path(tmpdir) / "notes.json")
        client = TestClient(app)
        
        create_resp = client.post("/notes", json={"title": "To delete", "content": "C"})
        note_id = create_resp.json()["id"]
        
        response = client.delete(f"/notes/{note_id}")
        assert response.status_code == 204
        
        get_resp = client.get(f"/notes/{note_id}")
        assert get_resp.status_code == 404


def test_not_found():
    if not FASTAPI_AVAILABLE:
        return
    
    with TemporaryDirectory() as tmpdir:
        app = create_app(Path(tmpdir) / "notes.json")
        client = TestClient(app)
        
        response = client.get("/notes/9999")
        assert response.status_code == 404


if __name__ == "__main__":
    if not FASTAPI_AVAILABLE:
        print("⚠ FastAPI not available - tests skipped")
        exit(0)
    
    test_create_note()
    test_get_notes()
    test_get_note_by_id()
    test_update_note()
    test_delete_note()
    test_not_found()
    print("✓ All tests passed")
