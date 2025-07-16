# Simple Rule-Based Chatbot

def chatbot():
    print("Chatbot: Hello! I'm your virtual assistant. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()

        if user_input in ["hello", "hi", "hey"]:
            print("Chatbot: Hi there! How can I help you?")
        
        elif "your name" in user_input:
            print("Chatbot: I'm a simple rule-based chatbot.")
        
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bunch of code, but I'm doing great! How about you?")
        
        elif "help" in user_input:
            print("Chatbot: Sure! I can help with basic queries. Ask me about time, weather, or just say hello.")
        
        elif "time" in user_input:
            from datetime import datetime
            now = datetime.now()
            print("Chatbot: The current time is", now.strftime("%H:%M:%S"))
        
        elif "weather" in user_input:
            print("Chatbot: I can't fetch live weather yet, but it's always sunny inside the code 😊")
        
        elif "bye" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        else:
            print("Chatbot: I'm not sure how to respond to that. Try asking something else.")

# Run the chatbot
chatbot()