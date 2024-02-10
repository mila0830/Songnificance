from openai import OpenAI
from dotenv import load_dotenv
import os
"""
file_path = "C:/Desktop/McWics Hackathon/Key.txt"
with open(file_path, "r") as file:
    API_KEY  = file.read()
    print(API_KEY)
"""
load_dotenv()

print(os.environ.get("OPENAI_API_KEY"))
client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY"))

chat_completion = client.chat.completions.create(
    messages = [
        {"role": "user",
          "content": "What is the meaning of the song eye of the tiger? in 3 sentenes"}
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion.choices[0].message.content)

