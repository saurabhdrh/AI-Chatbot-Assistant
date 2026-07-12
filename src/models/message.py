"""Message model for a single conversation message."""

from dataclasses import dataclass
from typing import Literal

Role = Literal["system", "user", "assistant"]


@dataclass(frozen=True)
class Message:
    """Represents one message in a conversation."""

    role: Role
    content: str

    def to_dict(self) -> dict[str, str]:
        """Convert the Message into the format expected by the LLM API."""
        return {
            "role": self.role,
            "content": self.content,
        }