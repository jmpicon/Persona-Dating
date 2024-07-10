# app/pdf_processing.py
from flask import Flask, request
from PyPDF2 import PdfReader
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/process', methods=['POST'])
def process_pdf():
    file = request.files['file']
    pdf_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(pdf_path)
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    os.remove(pdf_path)
    return text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
