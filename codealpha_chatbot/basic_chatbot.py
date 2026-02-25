import string


def clean_input(user_input):
    """
    Clean user input: lowercase, remove punctuation.
    """
    user_input = user_input.lower().strip()
    return user_input.translate(str.maketrans('', '', string.punctuation))


def chatbot_response(user_input):
    """
    Return response based on predefined rules and keywords.
    """
    user_input = clean_input(user_input)
    words = user_input.split()

    # Specific phrase responses first
    phrase_responses = {
        "how are you": "I'm doing great! Thanks for asking.",
        "what is your name": "I'm a simple Python chatbot.",
        "who created you": "I was created using Python as a practice project.",
        "thank you": "You're welcome!",
        "what time is it": "I can't tell the time yet.",
        "help": "You can greet me, ask my name, ask how I am, or say goodbye.",
        "what can you do": "I can chat with you using simple keyword-based responses.",
        "good morning": "Good morning! Hope you have a great day!",
        "good afternoon": "Good afternoon! How is your day going?",
        "good evening": "Good evening! How can I help you?"
    }

    for phrase, response in phrase_responses.items():
        if phrase in user_input:
            return response

    # General keyword responses
    greetings = ["hi", "hello", "hey", "yo"]
    farewells = ["bye", "goodbye", "see you"]
    thanks = ["thanks"]

    if any(word in words for word in greetings):
        return "Hi! How can I help you today?"

    if any(word in words for word in farewells):
        return "Goodbye! Have a great day."

    if any(word in words for word in thanks):
        return "You're welcome!"

    return "Sorry, I don't understand that."


def main():
    print("Chatbot is running! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)

        # Exit if user says goodbye
        if any(word in clean_input(user_input).split() for word in ["bye", "goodbye"]):
            break


if __name__ == "__main__":
    main()
