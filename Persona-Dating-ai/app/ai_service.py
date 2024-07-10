# app/ai_service.py
from flask import Flask, request, jsonify
from ollama import Chatbot

def load_chatbot_model():
    return Chatbot()

chatbot = load_chatbot_model()

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = chatbot.ask(user_input)
    return jsonify({'response': response['answer']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
