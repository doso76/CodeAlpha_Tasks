def chatbot_response(user_input):
    user_input = user_input.lower()

    greetings = ["hi", "hello", "yo"]

    if user_input in greetings:
        return "Hi! How can I help you?"

    elif user_input == "how are you":
        return "I'm good, thanks for asking"

    elif user_input == "bye":
        return "Goodbye, Have a nice day"

    elif user_input == "what is your name":
        return "I'm a simple Python chatbot."

    elif user_input == "who created you":
        return "I was created using Python as a practice project."

    elif user_input == "help":
        return "I can respond to greetings, basic questions, and goodbyes."

    elif user_input == "what can you do":
        return "I can chat with you using simple predefined responses."

    elif user_input in ("thank you", "thanks"):
        return "You're welcome!"

    elif user_input == "good morning":
        return "Good morning! Hope you have a great day."

    elif user_input == "good afternoon":
        return "Good afternoon! How is your day going?"

    elif user_input == "good evening":
        return "Good evening! How can I help you?"

    elif user_input == "what time is it":
        return "I can't tell the time yet, but I hope you're doing well."

    else:
        return "Sorry, I don't understand that."


print("Chatbot is running! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Bot:", response)

    if user_input.lower() == "bye":
        break
