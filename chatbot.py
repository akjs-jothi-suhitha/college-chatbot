print("Hello! I'm your college Assistant Chatbot.")
print("Type 'bye' to exit.\n")
while True:
    user_input=input("You: ").lower()
    if user_input in ['bye', 'exit']:
        print("Bot: Goodbye! All the best")
        break
    else:
        print("Bot: I'm still learning. Try asking me something simple.")