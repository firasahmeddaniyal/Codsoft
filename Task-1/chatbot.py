def chatbot_response(user_input):
    # Define some basic responses
    responses = {
        "hi": "Hello there .What can i do for you?",
        "how are you": "I'm fine, thanks.",
        "i want to ask you something": "Go ahead....",
        "are you human": "I'm not human or robot. I'm a software here to help you",
        "where are you": "I'm here.",
        "do you know siri": "Yes of course, she is a wonderful AI assistant.",
        "whats the weather like today?": "Sunny, 75°F.",
        "can you tell me a joke?": " Why don't scientists trust atoms? They make up everything!",
        "how do I cook pasta?": "Boil until firm but not hard; drain immediately.",
        "who made you": "I was designed by Daniyal & co.",
        "where do you live": "Home is where I am helpful",
        "bye": "Goodbye! Have a great day!",
        
    }
    
    # Check if user input matches any predefined responses
    if user_input.lower() in responses:
        return responses[user_input.lower()]
    else:
        return "I don't have an answer for that. Is there something else I can help with."

# Main function to interact with the chatbot
def main():
    print("Welcome to the Chatbot!")
    print("Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print(chatbot_response(user_input))
            break
        else:
            print("Bot:", chatbot_response(user_input))

# Start the conversation
if __name__ == "__main__":
    main()
