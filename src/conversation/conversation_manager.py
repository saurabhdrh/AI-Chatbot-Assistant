"""Conversation state management."""

from src.models.message import Message, Role
from src.prompts.system_prompt import SYSTEM_PROMPT


class ConversationManager:
    """Manages the conversation history."""

    def __init__(self) -> None:
        self.messages: list[Message] = self._initial_messages()

    @staticmethod
    def _initial_messages() -> list[Message]:
        return [Message(role="system", content=SYSTEM_PROMPT)]

    def _add(self, role: Role, content: str) -> None:
        self.messages.append(Message(role=role, content=content))

    def add_user_message(self, content: str) -> None:
        self._add("user", content)

    def add_assistant_message(self, content: str) -> None:
        self._add("assistant", content)

    def get_messages(self) -> list[dict[str, str]]:
        return [message.to_dict() for message in self.messages]

    def clear(self) -> None:
        self.messages = self._initial_messages()
