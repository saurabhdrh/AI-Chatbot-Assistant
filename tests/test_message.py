from src.models.message import Message

message = Message(
    role="user",
    content="Hello AI"
)

print(message)
print(message.to_dict())