from src.models.message import Message
from src.prompts.system_prompt import SYSTEM_PROMPT

class ConversationManager:
    """
    Manages the conversation history.
    """

    def __init__(self):
        self.messages = [
        Message(
            role="system",
            content=SYSTEM_PROMPT
        )
    ]

    def add_user_message(self, content: str):
        self.messages.append(
            Message(
                role="user",
                content=content
            )
        )

    def add_assistant_message(self, content: str):
        self.messages.append(
            Message(
                role="assistant",
                content=content
            )
        )

    def get_messages(self):
        return [
            message.to_dict()
            for message in self.messages
        ]

    def clear(self):
        self.messages = [
            Message(
                role="system",
                content=SYSTEM_PROMPT
            )
        ]
