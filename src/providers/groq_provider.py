"""Groq provider built on the OpenAI-compatible client."""

import os
from functools import lru_cache

from openai import OpenAI

from config import MAX_TOKENS, MODEL, TEMPERATURE

_GROQ_BASE_URL = "https://api.groq.com/openai/v1"
_REQUEST_TIMEOUT_SECONDS = 30.0


@lru_cache(maxsize=1)
def _get_client() -> OpenAI:
    """Create (once) and return the Groq client, failing fast if the key is missing."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY is not set. Add it to your environment or .env file."
        )
    return OpenAI(
        api_key=api_key,
        base_url=_GROQ_BASE_URL,
        timeout=_REQUEST_TIMEOUT_SECONDS,
    )


def ask_groq(messages: list[dict[str, str]]) -> str:
    """Send messages to Groq and return the assistant's reply text.

    Raises:
        RuntimeError: if GROQ_API_KEY is not configured.
        openai.OpenAIError: for API or network failures.
    """
    response = _get_client().chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
    )
    return response.choices[0].message.content or ""