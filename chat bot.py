# Customer Support + Friendly Chatbot
def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hello! Welcome to our customer support. How can I assist you today?"

    elif "how are you" in user_input:
        return "I'm doing great, thank you! How about you?"

    elif "fine" in user_input or "good" in user_input:
        return "Glad to hear that! What can I help you with today?"

    # Product Information
    elif "product" in user_input or "item" in user_input:
        return "Could you please specify which product you're asking about? I can give details, price, and availability."

    elif "price" in user_input:
        return "Please tell me the product name so I can share the price."

    elif "available" in user_input or "in stock" in user_input:
        return "Let me know the product name and I’ll check its availability."

    # Order Support
    elif "order status" in user_input or "track my order" in user_input:
        return "Sure! Please provide your order ID so I can check the status."

    elif "cancel order" in user_input:
        return "I can help with that. Please share your order ID to proceed."

    elif "return" in user_input or "refund" in user_input:
        return "Our return policy allows returns within 30 days of delivery. Please provide your order ID to start the process."

    # Billing & Payment
    elif "payment" in user_input or "billing" in user_input:
        return "Are you asking about payment methods or an issue with a recent payment?"

    elif "payment methods" in user_input:
        return "We accept credit cards, debit cards, PayPal, and net banking."

    elif "invoice" in user_input or "bill" in user_input:
        return "Please share your order ID and I can send your invoice."

    # Technical Support
    elif "issue" in user_input or "problem" in user_input or "error" in user_input:
        return "I’m sorry you’re facing this issue. Could you describe the problem in detail so I can help?"

    elif "app not working" in user_input:
        return "Please try restarting the app and checking your internet connection. If the problem persists, I’ll connect you to a technician."

    # Company Info
    elif "store hours" in user_input or "timings" in user_input:
        return "Our store is open from 9 AM to 9 PM, Monday to Saturday."

    elif "contact" in user_input or "phone number" in user_input:
        return "You can reach our customer support at +1-800-123-4567."

    elif "email" in user_input:
        return "You can email us at support@example.com."

    # Fun/Personal
    elif "joke" in user_input:
        return "Why don’t skeletons fight each other? They don’t have the guts!"

    elif "thank you" in user_input or "thanks" in user_input:
        return "You’re welcome! Happy to help."

    elif "bye" in user_input or "goodbye" in user_input or "see you" in user_input:
        return "Goodbye! Thank you for visiting us."

    else:
        return "I'm not sure I understand. Could you rephrase or give more details?"

# Main loop
def main():
    print("Chatbot: Hi! I am Venu Pasala, your friendly customer support chatbot. How can I help you today?")

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
