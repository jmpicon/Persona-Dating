import re

def filter_text(text):
    # Elimina las líneas vacías
    text = re.sub(r'\n\s*\n', '\n', text)
    
    # Elimina caracteres no deseados
    text = re.sub(r'[^A-Za-z0-9\s.,;!?]', '', text)
    
    # Filtra oraciones relevantes
    lines = text.split('\n')
    filtered_lines = [line for line in lines if len(line) > 10]  # Filtra líneas muy cortas que probablemente no son útiles
    
    filtered_text = '\n'.join(filtered_lines)
    return filtered_text
