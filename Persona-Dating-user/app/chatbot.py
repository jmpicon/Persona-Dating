# app/chatbot.py
from ollama import Chatbot

def load_chatbot_model():
    return Chatbot()

chatbot = load_chatbot_model()

def get_response(user_input):
    response = chatbot.ask(user_input)
    return response['answer']
