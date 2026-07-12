"""Runtime configuration for the chatbot.

Values default to sensible constants but can be overridden with environment
variables (loaded from a local .env file if present):

    PROVIDER      LLM provider name (default: "groq")
    MODEL         Model identifier (default: "qwen/qwen3-32b")
    TEMPERATURE   Sampling temperature, 0.0-2.0 (default: 0.3)
    MAX_TOKENS    Max tokens to generate, > 0 (default: 500)

Invalid values raise ValueError at import time so misconfiguration fails fast.
"""

import os

from dotenv import load_dotenv

load_dotenv()


def _get_float(name: str, default: float, minimum: float, maximum: float) -> float:
    raw = os.getenv(name)
    if raw is None:
        value = default
    else:
        try:
            value = float(raw)
        except ValueError as exc:
            raise ValueError(f"{name} must be a number, got {raw!r}") from exc

    if not minimum <= value <= maximum:
        raise ValueError(f"{name} must be between {minimum} and {maximum}, got {value}")
    return value


def _get_int(name: str, default: int, minimum: int) -> int:
    raw = os.getenv(name)
    if raw is None:
        value = default
    else:
        try:
            value = int(raw)
        except ValueError as exc:
            raise ValueError(f"{name} must be an integer, got {raw!r}") from exc

    if value < minimum:
        raise ValueError(f"{name} must be >= {minimum}, got {value}")
    return value


PROVIDER: str = os.getenv("PROVIDER", "groq")

MODEL: str = os.getenv("MODEL", "qwen/qwen3-32b")

TEMPERATURE: float = _get_float("TEMPERATURE", default=0.3, minimum=0.0, maximum=2.0)

MAX_TOKENS: int = _get_int("MAX_TOKENS", default=500, minimum=1)