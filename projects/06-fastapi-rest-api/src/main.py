"""FastAPI Task Notes API - Core."""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import json
from pathlib import Path


class Note(BaseModel):
    """Note model."""
    id: int
    title: str
    content: str
    tags: List[str] = []


class NoteCreate(BaseModel):
    """Note creation model."""
    title: str
    content: str
    tags: List[str] = []


class NoteStorage:
    """JSON-based storage."""
    
    def __init__(self, storage_path: Path):
        self.storage_path = storage_path
        self.notes: List[Note] = []
        self.load()
    
    def load(self):
        if self.storage_path.exists():
            with open(self.storage_path) as f:
                data = json.load(f)
                self.notes = [Note(**n) for n in data]
    
    def save(self):
        with open(self.storage_path, 'w') as f:
            json.dump([n.model_dump() for n in self.notes], f, indent=2)
    
    def create(self, note: NoteCreate) -> Note:
        note_id = max([n.id for n in self.notes], default=0) + 1
        new_note = Note(id=note_id, **note.model_dump())
        self.notes.append(new_note)
        self.save()
        return new_note
    
    def get_all(self) -> List[Note]:
        return self.notes
    
    def get_by_id(self, note_id: int) -> Optional[Note]:
        for note in self.notes:
            if note.id == note_id:
                return note
        return None
    
    def update(self, note_id: int, note_data: NoteCreate) -> Optional[Note]:
        note = self.get_by_id(note_id)
        if not note:
            return None
        note.title = note_data.title
        note.content = note_data.content
        note.tags = note_data.tags
        self.save()
        return note
    
    def delete(self, note_id: int) -> bool:
        note = self.get_by_id(note_id)
        if not note:
            return False
        self.notes.remove(note)
        self.save()
        return True


def create_app(storage_path: Path = Path("notes.json")) -> FastAPI:
    """Create FastAPI app."""
    app = FastAPI(title="Notes API", version="1.0")
    storage = NoteStorage(storage_path)
    
    @app.get("/")
    def root():
        return {"message": "Notes API - see /docs"}
    
    @app.get("/notes", response_model=List[Note])
    def list_notes():
        return storage.get_all()
    
    @app.get("/notes/{note_id}", response_model=Note)
    def get_note(note_id: int):
        note = storage.get_by_id(note_id)
        if not note:
            raise HTTPException(404, "Note not found")
        return note
    
    @app.post("/notes", response_model=Note, status_code=201)
    def create_note(note: NoteCreate):
        return storage.create(note)
    
    @app.put("/notes/{note_id}", response_model=Note)
    def update_note(note_id: int, note: NoteCreate):
        updated = storage.update(note_id, note)
        if not updated:
            raise HTTPException(404, "Note not found")
        return updated
    
    @app.delete("/notes/{note_id}", status_code=204)
    def delete_note(note_id: int):
        if not storage.delete(note_id):
            raise HTTPException(404, "Note not found")
    
    return app


if __name__ == "__main__":
    import uvicorn
    app = create_app()
    uvicorn.run(app, host="127.0.0.1", port=8000)
