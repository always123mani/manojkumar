# Simple AI Chatbot
print("Hello! I'm your first AI bot. What's your name?")
name = input("You: ")  # User types their name
print(f"Nice to meet you, {name}! How can I help you today?")

while True:  # Keeps the bot running
    user_input = input("You: ").lower()  # Convert input to lowercase

    if "hello" in user_input or "hi" in user_input:
        print("Bot: Hi there! 😊")
    elif "how are you" in user_input:
        print("Bot: I'm just a bot, but I'm doing great! How about you?")
    elif "bye" in user_input or "goodbye" in user_input:
        print("Bot: Goodbye! Have a nice day! 👋")
        break  # Exits the bot
    else:
        print("Bot: I'm still learning. Can you ask something else?")