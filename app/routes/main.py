from flask import Blueprint, render_template, request, redirect, url_for, jsonify
import os
from app.utils.pdf_to_csv import pdf_to_csv
from app.utils.chatbot import get_response

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
            csv_path = pdf_path.replace('.pdf', '.csv')
            file.save(pdf_path)
            pdf_to_csv(pdf_path, csv_path)
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
    return jsonify({'response': response})

