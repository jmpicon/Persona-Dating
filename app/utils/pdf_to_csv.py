import pandas as pd
from PyPDF2 import PdfReader

def pdf_to_csv(pdf_path, csv_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    data = {"text": [text]}
    df = pd.DataFrame(data)
    df.to_csv(csv_path, index=False)
