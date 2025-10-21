import streamlit as st
from PIL import Image

# --- CONFIGURACIÓN GENERAL ---
st.set_page_config(
    page_title="Aplicaciones de Inteligencia Artificial",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- TÍTULO PRINCIPAL ---
st.markdown(
    """
    <h1 style='text-align:center; color:#2E86C1;'>
        🤖 Aplicaciones de Inteligencia Artificial
    </h1>
    <p style='text-align:center; font-size:17px;'>
        Explora ejemplos reales de cómo la IA se aplica en voz, imagen, texto y datos.
    </p>
    <hr style='border:1px solid #2E86C1'>
    """,
    unsafe_allow_html=True
)

# --- SIDEBAR ---
with st.sidebar:
    st.header("💡 Sobre estas aplicaciones")
    parrafo = (
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
    )
    st.write(parrafo)
    st.info("📎 Cada aplicación abre en una nueva página desarrollada con Streamlit.")

# --- ENLACE PRINCIPAL ---
url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.markdown(
    f"""
    <div style='text-align:center; margin-bottom:30px;'>
        <h3>🔗 Recursos y ejercicios prácticos</h3>
        <p>Puedes acceder a más ejemplos en el siguiente enlace:</p>
        <a href="{url_ia}" target="_blank" style='font-size:18px; color:#117A65; font-weight:bold; text-decoration:none;'>Ir a las páginas y ejercicios →</a>
    </div>
    """,
    unsafe_allow_html=True
)

# --- COLUMNAS PRINCIPALES ---
col1, col2, col3 = st.columns(3)

# =======================
# COLUMNA 1
# =======================
with col1:
    st.markdown("###  Analizador Semántico en Español")
    image = Image.open('imagen_2025-10-21_160938233.png')
    st.image(image, use_container_width=True)
    st.write("Explora cómo la inteligencia artificial analiza similitudes entre textos usando TF-IDF, Ingresa tus documentos y una pregunta para descubrir cuál tiene la respuesta más cercana.")
    st.link_button("Abrir Analizador Esp", "https://fpjf47zlshrzwcsafmahnc.streamlit.app")

    st.divider()

    st.markdown("### 🎯 Analizador Emocional de texto")
    image = Image.open('emociones.png')
    st.image(image, use_container_width=True)
    st.write("Explora la emoción, tono y enfoque detrás de tus palabras")
    st.link_button("Abrir Analizador Emocional", "https://eth3kutqednvvf4mduxqel.streamlit.app")

    st.divider()

    st.markdown("### 🧠 Analizador de Sentimientos y Corrección de Texto")
    image = Image.open('senntimientos.jpg')
    st.image(image, use_container_width=True)
    st.write("Explora cómo TextBlob interpreta el tono emocional de tus palabras y mejora tu escritura en inglés con su sistema de corrección automática. ")
    st.link_button("Abrir Analizador de Sentimientos y Corrección de Texto", "https://scvxamkhdjwswtzyhwwnxq.streamlit.app")

# =======================
# COLUMNA 2
# =======================
with col2:
    st.markdown("### 🎙️ Conversión de voz a texto")
    image = Image.open('OIG8.jpg')
    st.image(image, use_container_width=True)
    st.write("Transcribe tu voz en texto automáticamente.")
    st.link_button("Abrir Voz a Texto", "https://traductor-ab0sp9f6fi.streamlit.app/")

    st.divider()

    st.markdown("### 📊 Análisis de Datos")
    image = Image.open('data_analisis.png')
    st.image(image, use_container_width=True)
    st.write("Analiza archivos de datos con ayuda de agentes inteligentes.")
    st.link_button("Abrir Analizador", "https://asistpy-csv.streamlit.app/")

    st.divider()

    st.markdown("### 🎧 Transcriptor de Audio y Video")
    image = Image.open('OIG3.jpg')
    st.image(image, use_container_width=True)
    st.write("Convierte audio o video en texto con precisión automática.")
    st.link_button("Abrir Transcriptor", "https://transcript-whisper.streamlit.app/")

# =======================
# COLUMNA 3
# =======================
with col3:
    st.markdown("### 📄 Generación en Contexto (RAG)")
    image = Image.open('Chat_pdf.png')
    st.image(image, use_container_width=True)
    st.write("Consulta documentos PDF y obtén respuestas precisas con RAG.")
    st.link_button("Abrir RAG", "https://chatpdf-cc.streamlit.app/")

    st.divider()

    st.markdown("### 🖼️ Análisis de Imagen")
    image = Image.open('OIG4.jpg')
    st.image(image, use_container_width=True)
    st.write("Describe y analiza imágenes con el modelo GPT-4 Vision.")
    st.link_button("Abrir Vision", "https://vision2-gpt4o.streamlit.app/")

    st.divider()

    st.markdown("### ⚙️ Sistema Ciberfísico")
    image = Image.open('OIG6.jpg')
    st.image(image, use_container_width=True)
    st.write("Explora cómo la IA puede interactuar con el entorno físico.")
    st.link_button("Abrir Sistema", "https://vision2-gpt4o.streamlit.app/")
