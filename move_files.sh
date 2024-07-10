#!/bin/bash

# Crear la estructura de directorios si no existen
mkdir -p Persona-Dating-web/app/static Persona-Dating-web/app/templates
mkdir -p Persona-Dating-user/app
mkdir -p Persona-Dating-back/app
mkdir -p Persona-Dating-ai/app

# Mueve los archivos de la aplicación web si existen
if [ -d "app/static" ]; then
  mv app/static/* Persona-Dating-web/app/static/
fi

if [ -d "app/templates" ]; then
  mv app/templates/* Persona-Dating-web/app/templates/
fi

if [ -f "requirements.txt" ]; then
  mv requirements.txt Persona-Dating-web/
fi

if [ -f "Dockerfile" ]; then
  mv Dockerfile Persona-Dating-web/
fi

# Crear y mover archivos para el servicio de usuario si existen
echo "flask" > Persona-Dating-user/requirements.txt
echo "transformers" >> Persona-Dating-user/requirements.txt

if [ -f "chatbot.py" ]; then
  mv chatbot.py Persona-Dating-user/app/
fi

if [ -f "user_management.py" ]; then
  mv user_management.py Persona-Dating-user/app/
fi

# Crear y mover archivos para el backend si existen
echo "flask" > Persona-Dating-back/requirements.txt
echo "PyPDF2" >> Persona-Dating-back/requirements.txt
echo "transformers" >> Persona-Dating-back/requirements.txt

if [ -f "pdf_processing.py" ]; then
  mv pdf_processing.py Persona-Dating-back/app/
fi

if [ -f "model_training.py" ]; then
  mv model_training.py Persona-Dating-back/app/
fi

# Crear y mover archivos para el servicio AI si existen
echo "flask" > Persona-Dating-ai/requirements.txt
echo "transformers" >> Persona-Dating-ai/requirements.txt

if [ -f "ai_service.py" ]; then
  mv ai_service.py Persona-Dating-ai/app/
fi

