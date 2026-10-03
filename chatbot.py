def chatbot_reply(message):
    message = message.lower().strip()

    if message == "hello":
        return "Hi! Nice to meet you."

    elif message == "how are you":
        return "I'm fine, thanks! How are you?"

    elif message == "bye":
        return "Goodbye! Have a great day."

    else:
        return "Sorry, I don't understand that."


print("Simple Chatbot")
print("Type 'bye' to end the conversation.")

while True:
    user_message = input("You: ")

    reply = chatbot_reply(user_message)
    print("Bot:", reply)

    if user_message.lower().strip() == "bye":
        break