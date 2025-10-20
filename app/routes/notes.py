from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict

router = APIRouter()

# Temporary in-memory DB
notes_db: Dict[int, dict] = {}

class NoteCreate(BaseModel):
    title: str
    content: str

class Note(NoteCreate):
    id: int

@router.post("/notes", response_model=Note)
def create_note(note: NoteCreate):
    note_id = len(notes_db) + 1
    notes_db[note_id] = note.dict()
    return {"id": note_id, **note.dict()}

@router.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int):
    if note_id not in notes_db:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"id": note_id, **notes_db[note_id]}
