def chatbot_response(user_input):
    user_input = user_input.lower()

    greeting = ["hi", "hello", "yo",]

    if user_input in greeting:
        return "Hi! How can i help you?"

    elif user_input == "How are you":
        return "I'm good, thanks for asking"

    elif user_input == "bye":
        return "Goodbye, Have a nice day"

    else:
        return "sorry, i dont understand that."


print("Chatbot is running! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Bot:", response)

    if user_input.lower() == "bye":
        break
