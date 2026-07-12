from src.conversation.conversation_manager import ConversationManager
from src.prompts.system_prompt import SYSTEM_PROMPT


def test_new_manager_starts_with_system_message():
    manager = ConversationManager()
    assert manager.get_messages() == [{"role": "system", "content": SYSTEM_PROMPT}]


def test_add_messages_preserves_role_and_order():
    manager = ConversationManager()
    manager.add_user_message("Hello")
    manager.add_assistant_message("Hi there")

    messages = manager.get_messages()
    assert messages[1] == {"role": "user", "content": "Hello"}
    assert messages[2] == {"role": "assistant", "content": "Hi there"}


def test_get_messages_returns_dicts():
    manager = ConversationManager()
    manager.add_user_message("Hello")
    assert all(isinstance(message, dict) for message in manager.get_messages())


def test_clear_resets_to_system_message():
    manager = ConversationManager()
    manager.add_user_message("Hello")
    manager.clear()
    assert manager.get_messages() == [{"role": "system", "content": SYSTEM_PROMPT}]