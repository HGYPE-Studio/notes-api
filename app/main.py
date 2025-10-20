# app/main.py
from fastapi import FastAPI
from app.routes import notes

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Notes API!"}

# This line must come AFTER you import notes
app.include_router(notes.router, prefix="/api", tags=["notes"])
