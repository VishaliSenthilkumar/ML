def simple_chatbot(user_input):
    predefined_questions = {
        "hi": "Hello there!",
        "how are you": "I'm good, thank you!",
        "what is your name": "My name is I BOT.",
        "who created you": "I was created by [Creator's Name].",
        "bye": "Goodbye! Have a great day!",
        "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
        "what is the weather today": "I'm sorry, I don't have access to weather information.",
        "can you help me": "Sure, I'll do my best to assist you.",
        "what's your favorite color": "I don't have the ability to see colors, but I appreciate all of them!",
        "where are you from": "I exist in the digital realm!",
        "what do you do": "I'm here to chat and provide information to the best of my ability.",
        "how old are you": "I don't have an age as I'm just a computer program!",
        "what is the meaning of life": "That's a deep question! The answer may vary for each individual.",
        "do you dream": "I don't sleep or dream as I am a computer program.",
        "what languages do you speak": "I communicate in human languages that I've been programmed to understand.",
        "what are your hobbies": "I don't have personal hobbies, but I enjoy helping and interacting with people!",
        # Add more predefined questions and responses here
    }

    user_input_lower = user_input.lower()

    for question in predefined_questions:
        if question in user_input_lower:
            return predefined_questions[question]

    return "I'm sorry, I don't understand that question."

def chat():
    print("Bot: Hello! I'm your chatbot. Type 'bye' to end the conversation.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break

        response = simple_chatbot(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
