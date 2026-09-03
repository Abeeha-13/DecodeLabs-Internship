def rule_based_chatbot():
    # Knowledge Base: Predefined inputs and responses
    knowledge_base = {
        "hello": "Hello! Welcome to DecodeLabs support. How can I assist you today?",
        "hi": "Hi there! How can I help you?",
        "who are you": "I am a Rule-Based AI Chatbot created for DecodeLabs Project 1.",
        "help": "You can ask me about help, options, or support.",
        "options": "I can respond to greetings, provide information about myself, and provide basic support.",
        "support": "For support, please contact the DecodeLabs team.",
        "thanks": "You're very welcome! Let me know if you need anything else.",
        "thank you": "Happy to help!"
    }

    # Welcome message
    print("--- DecodeLabs Rule-Based AI Chatbot Active ---")
    print("Chatbot: Hello! I am ready to assist you.")
    print("Chatbot: Type 'help' to see what I can do.")
    print("Chatbot: Type 'exit', 'bye', or 'quit' to close the chatbot.\n")

    # Continuous loop
    while True:

        # Take input from the user
        raw_input = input("User: ")

        # Normalize the input
        clean_input = raw_input.lower().strip()

        # Exit commands
        if clean_input == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break

        elif clean_input == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break

        elif clean_input == "quit":
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Greeting rules
        elif clean_input == "hello":
            print("Chatbot:", knowledge_base["hello"])

        elif clean_input == "hi":
            print("Chatbot:", knowledge_base["hi"])

        # Information rules
        elif clean_input == "who are you":
            print("Chatbot:", knowledge_base["who are you"])

        elif clean_input == "help":
            print("Chatbot:", knowledge_base["help"])

        elif clean_input == "options":
            print("Chatbot:", knowledge_base["options"])

        # Support rule
        elif clean_input == "support":
            print("Chatbot:", knowledge_base["support"])

        # Thank-you rules
        elif clean_input == "thanks":
            print("Chatbot:", knowledge_base["thanks"])

        elif clean_input == "thank you":
            print("Chatbot:", knowledge_base["thank you"])

        # Default response for unknown input
        else:
            print(
                "Chatbot: I'm sorry, I don't understand that request yet. "
                "Try asking 'help' or 'options'."
            )

        print()


# Start the chatbot
if __name__ == "__main__":
    rule_based_chatbot()