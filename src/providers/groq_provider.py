from openai import OpenAI
from dotenv import load_dotenv
import os

from config import MODEL, TEMPERATURE, MAX_TOKENS

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def ask_groq(messages):

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS
    )

    return response