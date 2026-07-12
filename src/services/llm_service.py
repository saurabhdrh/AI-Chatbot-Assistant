"""Service layer that routes chat requests to the configured provider."""

from config import PROVIDER
from src.providers.groq_provider import ask_groq


def ask_llm(messages: list[dict[str, str]]) -> str:
    """Route messages to the configured provider and return the reply text.

    Raises:
        ValueError: if the configured provider is not supported.
    """
    if PROVIDER == "groq":
        return ask_groq(messages)

    raise ValueError(f"Unsupported provider: {PROVIDER}")