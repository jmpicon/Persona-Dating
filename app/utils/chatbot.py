from transformers import pipeline
import os

def update_chatbot_model():
    global chatbot
    model_path = "fine_tuned_model" if os.path.exists("fine_tuned_model") else "gpt2"
    chatbot = pipeline('text-generation', model=model_path)

update_chatbot_model()
