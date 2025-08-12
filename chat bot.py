# Extended Rule-based Chatbot
def chatbot_response(user_input):
    user_input = user_input.lower()

    # Define more rules and responses
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hello! How can I assist you today?"

    elif "how are you" in user_input:
        return "I'm doing great, thank you! How about you?"

    elif "fine" in user_input or "good" in user_input or "great" in user_input:
        return "Glad to hear that! How can I help you today?"

    elif "what's your name" in user_input or "who are you" in user_input:
        return "I am Venu Pasala, your friendly rule-based chatbot."

    elif "bye" in user_input or "goodbye" in user_input or "see you" in user_input:
        return "Goodbye! Take care and have a wonderful day!"

    elif "what can you do" in user_input or "help" in user_input:
        return "I can chat with you, answer simple questions, and keep you company!"

    elif "time" in user_input:
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."

    elif "date" in user_input or "day" in user_input:
        from datetime import datetime
        return f"Today is {datetime.now().strftime('%A, %B %d, %Y')}."

    elif "weather" in user_input:
        return "I can't check live weather yet, but I can chat with you about sunny or rainy days!"

    elif "joke" in user_input:
        return "Why don’t skeletons fight each other? They don’t have the guts!"

    elif "your creator" in user_input or "who made you" in user_input:
        return "I was created by Venu Pasala for friendly conversations."

    elif "favorite color" in user_input:
        return "I love blue — it reminds me of the clear sky!"

    elif "favorite food" in user_input:
        return "I don’t eat, but if I could, I’d try pizza first!"

    elif "where are you from" in user_input:
        return "I live inside your computer, always ready to chat!"

    elif "openai" in user_input:
        return "OpenAI is an AI research lab that created ChatGPT — I’m inspired by it!"

    else:
        return "I'm not sure I understand. Can you try asking in a different way?"

# Main loop for user interaction
def main():
    print("Chatbot: Hi! I am Venu Pasala, your friendly chatbot. How can I assist you today?")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            response = chatbot_response(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    main()
