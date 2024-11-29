from tkinter import *
import random
from datetime import datetime

# Function to handle user input and generate bot response
def respond():
    user_input = user_input_field.get()
    user_input = user_input.lower()

    # Emotion-based responses
    emotions = {
        "happy": "I'm glad to hear you're happy! 😊",
        "sad": "I'm sorry to hear that. I hope things get better soon! 😢",
        "angry": "Take a deep breath! Let’s try to stay calm. 😌",
        "excited": "That’s awesome! I can feel the energy! 😄",
        "bored": "It happens! Want to chat or hear a joke? 😊",
    }

    # Enhanced predefined responses
    responses = {
        "hello": "Hi! How can I assist you today?",
        "hi": "Hello there! How can I help you?",
        "how are you": "I'm doing great, thank you for asking! How about you?",
        "i'm fine": "I'm glad to hear you're doing well!",
        "bye": "Goodbye! Have a great day!",
        "your name": "I am a chatbot created to help you with anything you need!",
        "what is your purpose": "I was created to assist with your queries and chat with you!",
        "what can you do": "I can chat with you, answer basic questions, and provide assistance!",
        "who created you": "I was created by a group of developers to assist people like you.",
        "what is the weather": "Sorry, I can't check the weather right now. Please check on a weather website or app.",
        "tell me a joke": "Why don’t skeletons fight each other? They don’t have the guts!",
        "what is your favorite color": "I don't have a favorite color, but I think all colors are beautiful!",
        "what is the time": f"The current time is {datetime.now().strftime('%H:%M:%S')}.",
        "what is the date": f"Today's date is {datetime.now().strftime('%B %d, %Y')}.",
        "do you like music": "I think music is wonderful! It can make people feel so many emotions.",
        "what is the capital of france": "The capital of France is Paris.",
        "what is 2+2": "2+2 is 4.",
        "what is the meaning of life": "The meaning of life is a philosophical question, and everyone has their own view. Some say it's about love, others about happiness.",
        "what is your favorite food": "I don't eat, but I think pizza is a popular choice among people!",
        "how old are you": "I don't have an age like humans do, but I was created recently!",
        "tell me something interesting": "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient tombs that are over 3000 years old and still perfectly edible!",
        "can you help me": "Yes, I can help you with many things! Just let me know what you need.",
        "how do you work": "I work by using pre-programmed responses and patterns to interact with you. Think of me as a helper!",
        "tell me a story": "Once upon a time, in a faraway land, there was a dragon who loved to read books. One day, he discovered a magical book that granted him the ability to talk to humans!",
        "help": "You can ask me things like 'What is your name?', 'Tell me a joke', 'What is the time?', or even ask for a story!",
    }

    # Check for emotional responses
    for emotion in emotions:
        if emotion in user_input:
            bot_response = emotions[emotion]
            break
    else:
        # If the user's input matches a predefined response, return that response
        for key in responses:
            if key in user_input:
                bot_response = responses[key]
                break
        else:
            # If no match is found, return a random response
            bot_response = random.choice([
                "Sorry, I didn't understand that.",
                "Can you please rephrase your question?",
                "I'm not sure about that. Can you ask something else?",
                "I am still learning, so I might not know the answer to that."
            ])

    # Display the response in the chat box without labeling the speaker
    chat_box.insert(END, user_input + "\n")  # Display the user's input
    chat_box.insert(END, bot_response + "\n")  # Display the bot's response
    chat_box.yview(END)  # Scroll to the bottom to show the latest conversation

    # Clear the input field
    user_input_field.delete(0, END)

# Function to clear the chat window
def clear_chat():
    chat_box.delete(1.0, END)

# Setting up the Tkinter window
root = Tk()
root.title("Advanced Chatbot")
root.geometry("500x600")

# Creating the chat box to display conversation
chat_box = Text(root, height=20, width=50, bd=2, font=("Arial", 12))
chat_box.pack(padx=10, pady=10)

# Creating the user input field
user_input_field = Entry(root, width=50, font=("Arial", 12))
user_input_field.pack(padx=10, pady=10)

# Creating the send button
send_button = Button(root, text="Send", font=("Arial", 12), command=respond)
send_button.pack(pady=10)

# Creating the clear chat button
clear_button = Button(root, text="Clear Chat", font=("Arial", 12), command=clear_chat)
clear_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()

