from openai import OpenAI
from dotenv import load_dotenv
import os

"""
file_path = "C:/Desktop/McWics Hackathon/Key.txt"
with open(file_path, "r") as file:
    API_KEY  = file.read()
    print(API_KEY)
"""
def summarize_song(artist, track, year):
    load_dotenv()

    
    client = OpenAI(
        api_key = os.environ.get("OPENAI_API_KEY"))

    chat_completion = client.chat.completions.create(
        messages = [
            {"role": "user",
            "content": f"What is the meaning of the song {track} by {artist}? in 3 sentenes"}
        ],
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content

def summarize_lyrics(lyrics):
    load_dotenv()
    client = OpenAI(
        api_key = os.environ.get("OPENAI_API_KEY"))
    chat_completion = client.chat.completions.create(
        messages = [
            {"role": "user",
            "content": f"What is the meaning behind these lyrics: {lyrics}? in 3 sentenes"}
        ],
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content

