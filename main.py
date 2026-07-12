from src.conversation.conversation_manager import ConversationManager
from src.services.llm_service import ask_llm

conversation = ConversationManager()

print("=" * 50)
print(" Welcome to My AI Chatbot ")
print("=" * 50)
print("Type /exit to quit.\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "/exit":
        print("\n👋 Goodbye!")
        break
    conversation.add_user_message(user_input)
    response = ask_llm(conversation.get_messages())
    answer = response.choices[0].message.content
    conversation.add_assistant_message(answer)
    print(f"\nAI: {answer}\n")

print(f"\nMemory: {conversation.get_messages()}\n")
usage = response.usage

print("Token Usage")
print("-" * 20)
print(f"Prompt Tokens     : {usage.prompt_tokens}")
print(f"Completion Tokens : {usage.completion_tokens}")
print(f"Total Tokens      : {usage.total_tokens}")
print()



# from src.services.llm_service import ask_llm

# print("=" * 50)
# print("Welcome to My First AI Chatbot")
# print("=" * 50)

# question = input("\nYou: ")

# response = ask_llm(question)
# print("\nAssistant:")
# print(response.choices[0].message.content)
# print("\nToken Usage")
# print("-" * 20)

# print(f"Prompt Tokens     : {response.usage.prompt_tokens}")
# print(f"Completion Tokens : {response.usage.completion_tokens}")
# print(f"Total Tokens      : {response.usage.total_tokens}")
