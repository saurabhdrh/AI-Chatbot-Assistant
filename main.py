from src.conversation.conversation_manager import ConversationManager
from src.services.llm_service import ask_llm
def show_help():
    print("\nAvailable Commands")
    print("------------------------")
    print("/help  - Show help")
    print("/clear - Clear conversation")
    print("/exit  - Exit chatbot")
    print()

conversation = ConversationManager()

print("=" * 50)
print(" Welcome to My AI Chatbot ")
print("=" * 50)
print("Type /help for help.\n")
print("Type /clear to clear history.\n")
print("Type /exit to quit.\n")

while True:
    try:
        user_input = input("You: ").strip()
        
        if user_input.lower() == "/help":
            show_help()
            continue
        if user_input.lower() == "/clear":
            conversation.clear()
            print("Conversation cleared.")
            continue
        if user_input.lower() == "/exit":
            print("\n Goodbye!")
            break
    except Exception as e:
            print("\n Something went wrong.")
            print(f"Reason: {e}")

    conversation.add_user_message(user_input)
    response = ask_llm(conversation.get_messages())
    answer = response.choices[0].message.content
    conversation.add_assistant_message(answer)
    print(f"\nAI: {answer}\n")

print(f"\nMemory: {conversation.get_messages()}\n")
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
