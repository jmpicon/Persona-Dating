FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001 5003

CMD ["python", "app/pdf_processing.py"]
