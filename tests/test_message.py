from src.models.message import Message


def test_to_dict_returns_expected_shape():
    message = Message(role="user", content="Hello AI")
    assert message.to_dict() == {"role": "user", "content": "Hello AI"}


def test_to_dict_with_empty_content():
    message = Message(role="assistant", content="")
    assert message.to_dict() == {"role": "assistant", "content": ""}


def test_messages_are_equal_by_value():
    assert Message(role="user", content="hi") == Message(role="user", content="hi")