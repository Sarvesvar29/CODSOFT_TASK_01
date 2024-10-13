import re

def simple_chatbot(user_input):
    user_input = user_input.lower()
    
    if re.search(r'hello|hi|hey', user_input):
        return "Hello! How can I assist you today?"
    
    elif re.search(r'how are you', user_input):
        return "I'm just a program, but I'm doing great! How about you?"
    
    elif re.search(r'what is your name', user_input):
        return "I'm a simple chatbot built using Python! What's your name?"
    
    elif re.search(r'bye|goodbye', user_input):
        return "Goodbye! Have a nice day!"
    
    elif re.search(r'time', user_input):
        return "I can't check the time, but you can look at your system clock!"
    
    elif re.search(r'weather', user_input):
        return "I don't have access to live weather updates right now."
    
    else:
        return "Sorry, I didn't understand that. Can you please rephrase?"

while True:
    user_input = input("You: ")
    if user_input.lower() in ['bye', 'exit', 'quit']:
        print("Chatbot: Goodbye! Have a nice day!")
        break
    
    response = simple_chatbot(user_input)
    print(f"Chatbot: {response}")
