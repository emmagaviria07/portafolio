import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="Aplicaciones de Inteligencia Artificial",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


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


with st.sidebar:
    st.header("💡 Sobre estas aplicaciones")
    parrafo = (
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
    )
    st.write(parrafo)
    st.info("📎 Cada aplicación abre en una nueva página desarrollada con Streamlit.")

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


with col2:
    st.markdown("### 🎙️ Traductor")
    image = Image.open('ebbacd691475f0a6f7d43d7be15472aa.jpg')
    st.image(image, use_container_width=True)
    st.write("Habla y deja que la IA traduzca tu voz a otro idioma 🌍.")
    st.link_button("Abrir Traductor", "https://traductor-mnd2sehjafc6r7kr2fmx3m.streamlit.app")

    st.divider()

    st.markdown("### 📊 Draw Recognition")
    image = Image.open('b7aff56aca12d85062f2a1f8a6e080ce.jpg')
    st.image(image, use_container_width=True)
    st.write("Dibuja algo, presiona “Analizar la imagen”, y observa cómo el modelo lo describe. ")
    st.link_button("Abrir Draw Recognition", "https://drawrecog-9y2tfmeapp7uj8qdem9p2kl.streamlit.app")

    st.divider()

    st.markdown("### 🎧 Chat PDF")
    image = Image.open('6b6dd5a171abf33c000b1ddb83bb4fe2.jpg')
    st.image(image, use_container_width=True)
    st.write("Este asistente utiliza RAG (Retrieval-Augmented Generation) para responder preguntas basadas en el contenido de un PDF. Sube un documento, haz una pregunta, y deja que el modelo te dé una respuesta contextualizada. 📘✨")
    st.link_button("Abrir Chat PDF", "https://chatpdf-hq3ejh6xa6ar6xmjmujbjh.streamlit.app")

with col3:
    st.markdown("### 📄 Análisis de Imagen")
    image = Image.open('53e2de66257f04782768afcd09a5fc9d.jpg')
    st.image(image, use_container_width=True)
    st.write("Herramienta interactiva que analiza imágenes usando modelos de OpenAI.")
    st.link_button("Abrir Analizador", "https://imagen-texto-gfbubhzt3xgvzwjjnxlbqj.streamlit.app")

    st.divider()

    st.markdown("### 🖼️ Teachable Machine")
    image = Image.open('2a9847d15807e6bc8037c57afa472967.jpg')
    st.image(image, use_container_width=True)
    st.write("Usa un modelo entrenado en Teachable Machine para identificar objetos o gestos desde tu cámara.")
    st.link_button("Techable Machine", "https://cypc5gqb9zkxspyvuz6l6q.streamlit.app")

    st.divider()

    st.markdown("### ⚙️ Conversión de Texto a Audio")
    image = Image.open('1f14b442c7ba1c4da0d01abb883c3831.jpg')
    st.image(image, use_container_width=True)
    st.write("Esrcibe y/o selecciona texto para ser escuchado.")
    st.link_button("Abrir", "https://vozatexto-cuento-7prvibeydfnkmbzvfnbf8p.streamlit.app")



st.markdown("---")  # Línea divisoria para separar visualmente la nueva sección

st.markdown(
    """
    <h2 style='text-align:center; color:#1A5276;'>
        🚀 Intro de las apps 
    </h2>
    <p style='text-align:center; font-size:16px;'>
        La puse al final :)
    </p>
    """,
    unsafe_allow_html=True
)

# Centrado de contenido (imagen + botón)
col_a, col_b, col_c = st.columns([1, 2, 1])  
with col_b:
    image = Image.open("imagen_2025-10-21_164905350.png")  
    st.image(image, use_container_width=True)
    st.write(
        "<p style='text-align:center;'>Aca empezamos.</p>",
        unsafe_allow_html=True
    )
    st.link_button("Abrir Intro", "https://appemma.streamlit.app")  

