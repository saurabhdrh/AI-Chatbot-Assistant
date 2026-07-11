from config import PROVIDER

from src.providers.groq_provider import ask_groq


def ask_llm(messages):

    if PROVIDER == "groq":
        return ask_groq(messages)

    raise ValueError(f"Unsupported provider: {PROVIDER}")