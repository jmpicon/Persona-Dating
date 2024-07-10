from flask import Blueprint, render_template, request, redirect, url_for, jsonify
import os
from app.utils.pdf_to_text import pdf_to_text
from app.utils.filter_text import filter_text
from app.utils.update_model import fine_tune_model
from app.utils.chatbot import update_chatbot_model, get_response
from app.models import db, Interaction

main = Blueprint('main', __name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            pdf_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(pdf_path)
            extracted_text = pdf_to_text(pdf_path)
            filtered_text = filter_text(extracted_text)
            fine_tune_model(filtered_text)
            update_chatbot_model()
            return redirect(url_for('main.home'))
    return '''
    <!doctype html>
    <title>Upload PDF</title>
    <h1>Upload PDF</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@main.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = get_response(user_input)
    interaction = Interaction(user_id=1, question=user_input, response=response)  # Suponiendo user_id=1 para simplificar
    db.session.add(interaction)
    db.session.commit()
    return jsonify({'response': response})
