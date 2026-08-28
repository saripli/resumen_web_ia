# imports

import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
from openai import OpenAI
#import ollama

# Inicialización y constantes and constants
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

if api_key and api_key[:8]=='sk-proj-':
    print("La clave de API parece buena")
else:
    print("¿Puede haber un problema con tu clave API? ¡Visita el cuaderno de resolución de problemas!")
    
MODEL = 'gpt-4o-mini'
openai = OpenAI()

# Una clase para representar una página web
# Si no estás familiarizado con las clases, consulta el cuaderno "Python intermedio"

class Website:
    """
    Una clase de utilidad para representar un sitio web que hemos scrappeado
    """

    def __init__(self, url:str):
        """
        Crea este objeto de sitio web a partir de la URL indicada utilizando la biblioteca BeautifulSoup
        """
        self.url = url
        
        # Simulamos un navegador real para evitar bloqueos 403
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No tiene título"
        for irrelevant in soup.body(["script", "style", "img", "input","nav","footer"]):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)

# Prompts
system_prompt = "Eres un asistente que analiza el contenido de un sitio web \
y proporciona un breve resumen, ignorando el texto que podría estar relacionado con la navegación. \
Responder en Markdown."

# Una función que escribe un mensaje de usuario que solicita resúmenes de sitios web:
def user_prompt_for(website):
    user_prompt = f"Estás viendo un sitio web titulado {website.title}"
    user_prompt += "\nEl contenido de este sitio web es el siguiente; \
    proporciona un breve resumen de este sitio web en formato Markdown. \
    Si incluye noticias, productos o anuncios, resúmelos también.\n\n"
    user_prompt += website.text
    return user_prompt

# Puedes ver cómo esta función crea exactamente el formato anterior
def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(website)}
    ]

# Y ahora: llama a la API de OpenAI. ¡Te resultará muy familiar!
def summarize(url):
    website = Website(url)
    response = openai.chat.completions.create(
        model = MODEL,
        messages = messages_for(website)
    )
    return response.choices[0].message.content

# Una función para mostrar esto de forma clara en la salida de Jupyter, usando markdown
def display_summary(url):
    """
    Muestra el resumen formateado
    """
    summary = summarize(url)
    display(Markdown(summary))

if __name__ == "__main__":
    url = "https://es.wikipedia.org/wiki/Inteligencia_artificial"
    resumen = summarize(url)
    print("\n--- RESUMEN OBTENIDO ---\n")
    print(resumen)

