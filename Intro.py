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


)

# --- COLUMNAS PRINCIPALES ---
col1, col2, col3 = st.columns(3)

# =======================
# COLUMNA 1
# =======================
with col1:
    st.markdown("### 🗣️ Conversión de texto a voz")
    image = Image.open('txt_to_audio2.png')
    st.image(image, use_container_width=True)
    st.write("Convierte texto escrito en voz humana con IA.")
    st.link_button("Abrir Texto a Voz", "https://imultimod.streamlit.app/")

    st.divider()

    st.markdown("### 🎯 Reconocimiento de Objetos")
    image = Image.open('txt_to_audio.png')
    st.image(image, use_container_width=True)
    st.write("Detecta y clasifica objetos en imágenes con YOLO.")
    st.link_button("Abrir YOLO", "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/")

    st.divider()

    st.markdown("### 🧠 Entrenando Modelos")
    image = Image.open('OIG5.jpg')
    st.image(image, use_container_width=True)
    st.write("Usa tus propios modelos entrenados en Teachable Machine.")
    st.link_button("Abrir Modelo", "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/")

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

