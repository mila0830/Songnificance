from fastapi import FastAPI, HTTPException
from typing import Annotated
from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from enum import Enum
from clientcredit import get_summary_with_track_and_artist
from clientcredit import get_token

class Input(BaseModel):
    song: str
    artist: str
    summary: str

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/results")
async def create_item(song: str= Form(...), artist: str=Form(...)):
    token = get_token()
    summary = (get_summary_with_track_and_artist(token, song, artist))
    return {
        "song": song,
        "artist": artist,
        "summary": summary,
        
    }