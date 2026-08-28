# 🌐 Web Content Summarizer with OpenAI

Herramienta en Python que realiza web scraping de páginas y artículos web con **BeautifulSoup** y genera resúmenes estructurados, limpios y concisos utilizando la API de **OpenAI** (`gpt-4o-mini`).

---

## 📌 Descripción del Proyecto

Este proyecto resuelve el problema de sintetizar rápidamente artículos largos y documentación web. El script realiza las siguientes tareas:
1. Descarga el código HTML simulando un navegador real mediante cabeceras HTTP personalizadas (`User-Agent`) para evitar bloqueos.
2. Limpia el contenido eliminando elementos prescindibles (scripts, estilos CSS, barras de navegación y pies de página).
3. Envía el texto procesado al modelo `gpt-4o-mini` con un prompt optimizado para extraer los puntos clave.
4. Muestra la respuesta en formato Markdown claro y estructurado.

---

## 🛠️ Tecnologías y Librerías

* **Lenguaje:** Python 3.10+
* **LLM:** OpenAI API (`gpt-4o-mini`)
* **Scraping & Parsing:** `BeautifulSoup4`, `requests`
* **Gestión de variables de entorno:** `python-dotenv`
* **Visualización:** `ipython` (compatible con Jupyter y terminal estándar)

---

## 📁 Estructura del Repositorio

```text
Mi_primer_proyecto/
├── .env                  # Variables de entorno y API Keys (ignorado por Git)
├── .env.example          # Plantilla de configuración de variables
├── .gitignore            # Archivos y carpetas excluidos del control de versiones
├── requirements.txt      # Dependencias del proyecto
├── main.py               # Código fuente principal
└── README.md             # Documentación del proyecto