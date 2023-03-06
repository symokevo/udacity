import random

# Define a list of potential bot responses
bot_responses = [
    "Hello, how can I help you today?",
    "What can I do for you?",
    "How are you doing?",
    "I'm here to assist you.",
    "Is there anything you need help with?"
]

# Define a function to generate bot responses
def generate_bot_response():
    return random.choice(bot_responses)

# Main loop for the chat bot
while True:
    user_input = input("User: ")
    if user_input.lower() == 'exit':
        print("Bot: Goodbye!")
        break
    else:
        bot_response = generate_bot_response()
        print("Bot: " + bot_response)
