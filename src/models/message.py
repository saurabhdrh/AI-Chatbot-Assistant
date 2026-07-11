from dataclasses import dataclass
@dataclass
class Message:
    """
    Represents one message in a conversation.
    """

    role: str
    content: str

    def to_dict(self) -> dict:
        """
        Convert the Message object into the format expected by the LLM API.
        """
        return {
            "role": self.role,
            "content": self.content
        }