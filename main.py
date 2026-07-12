"""Interactive command-line chatbot entry point."""

from src.conversation.conversation_manager import ConversationManager
from src.services.llm_service import ask_llm
from src.utils.logger import logger


def show_help() -> None:
    print("\nAvailable Commands")
    print("------------------------")
    print("/help  - Show help")
    print("/clear - Clear conversation")
    print("/exit  - Exit chatbot")
    print()


def print_welcome() -> None:
    print("=" * 50)
    print(" Welcome to My AI Chatbot ")
    print("=" * 50)
    print("Type /help for help.")
    print("Type /clear to clear history.")
    print("Type /exit to quit.\n")


def run_chat() -> None:
    conversation = ConversationManager()
    print_welcome()
    logger.info("Chat session started.")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        command = user_input.lower()
        if command == "/help":
            show_help()
            continue
        if command == "/clear":
            conversation.clear()
            print("Conversation cleared.")
            continue
        if command == "/exit":
            print("\nGoodbye!")
            break

        conversation.add_user_message(user_input)

        try:
            answer = ask_llm(conversation.get_messages())
        except Exception as exc:  # surface any provider/network error, keep chatting
            logger.exception("Error while contacting the AI provider.")
            print(f"\nSomething went wrong while contacting the AI: {exc}\n")
            continue

        conversation.add_assistant_message(answer)
        print(f"\nAI: {answer}\n")


def main() -> None:
    run_chat()


if __name__ == "__main__":
    main()
