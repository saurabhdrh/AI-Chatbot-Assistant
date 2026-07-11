from src.conversation.conversation_manager import ConversationManager


conversation = ConversationManager()

conversation.add_user_message("Hello")

conversation.add_assistant_message("Hi Mukul!")

conversation.add_user_message("How are you?")

print(conversation.get_messages())