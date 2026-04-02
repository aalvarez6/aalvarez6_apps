import streamlit as st
from PIL import Image

# ── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Aplicaciones de IA",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── APPLE-STYLE CSS ───────────────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@300;400;500;600;700&display=swap');
  /* Fallback: use system-ui which maps to SF Pro on Apple devices */

  html, body, [class*="css"] {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }

  /* ── Background ── */
  .stApp {
    background: #f5f5f7;
  }

  /* ── Sidebar ── */
  [data-testid="stSidebar"] {
    background: rgba(255,255,255,0.85);
    backdrop-filter: blur(20px);
    border-right: 1px solid rgba(0,0,0,0.08);
  }
  [data-testid="stSidebar"] .stMarkdown p {
    font-size: 0.88rem;
    color: #3a3a3c;
    line-height: 1.6;
  }

  /* ── Main title ── */
  h1 {
    font-size: 2.4rem !important;
    font-weight: 700 !important;
    letter-spacing: -0.5px !important;
    color: #1d1d1f !important;
    margin-bottom: 0.2rem !important;
  }

  /* ── Card container ── */
  .app-card {
    background: #ffffff;
    border-radius: 18px;
    padding: 16px 16px 14px;
    margin-bottom: 20px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.07);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    height: 100%;
  }
  .app-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.12);
  }

  /* ── Card image ── */
  .app-card img {
    width: 100% !important;
    height: 160px !important;
    object-fit: cover !important;
    border-radius: 12px !important;
    display: block;
  }

  /* ── Card title ── */
  .card-title {
    font-size: 0.95rem;
    font-weight: 600;
    color: #1d1d1f;
    margin: 10px 0 4px;
    line-height: 1.3;
  }

  /* ── Card description (3 lines max) ── */
  .card-desc {
    font-size: 0.78rem;
    color: #6e6e73;
    line-height: 1.45;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
    margin-bottom: 8px;
  }

  /* ── Card link ── */
  .card-link a {
    font-size: 0.8rem;
    font-weight: 500;
    color: #0071e3;
    text-decoration: none;
  }
  .card-link a:hover {
    text-decoration: underline;
  }

  /* ── Section divider ── */
  .section-label {
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #6e6e73;
    margin: 32px 0 12px;
  }

  /* ── Pill badge ── */
  .badge {
    display: inline-block;
    background: #e8f0fe;
    color: #0071e3;
    font-size: 0.68rem;
    font-weight: 600;
    border-radius: 20px;
    padding: 2px 9px;
    margin-bottom: 6px;
  }

  /* ── Hide Streamlit branding ── */
  #MainMenu, footer {visibility: hidden;}
  .block-container {padding-top: 2.2rem; padding-bottom: 2rem;}
</style>
""", unsafe_allow_html=True)


# ── HELPER: render one card ───────────────────────────────────────────────────
def card(title: str, img_path: str, desc: str, url: str, badge: str = ""):
    badge_html = f'<div class="badge">{badge}</div>' if badge else ""
    try:
        img = Image.open(img_path).resize((400, 240))
        st.image(img, use_container_width=True)
    except Exception:
        st.image("https://placehold.co/400x240/e8e8ed/6e6e73?text=Preview",
                 use_container_width=True)

    st.markdown(f"""
    <div>
      {badge_html}
      <div class="card-title">{title}</div>
      <div class="card-desc">{desc}</div>
      <div class="card-link"><a href="{url}" target="_blank">Abrir aplicación →</a></div>
    </div>
    """, unsafe_allow_html=True)


# ── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🤖 Inteligencia Artificial")
    st.markdown("""
    La IA mejora la toma de decisiones con datos, automatiza tareas rutinarias
    y ofrece análisis avanzados en tiempo real, logrando mayor eficiencia en
    múltiples campos.
    """)
    st.markdown("---")
    url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
    st.markdown(f"📚 [Páginas y ejercicios]({url_ia})")
    st.markdown("---")
    st.caption("Versión 2.0 · Estilo Apple")


# ── HEADER ────────────────────────────────────────────────────────────────────
st.markdown("## 🤖 Aplicaciones de Inteligencia Artificial")
st.markdown(
    "<p style='color:#6e6e73;font-size:1rem;margin-top:-8px;'>"
    "Explora herramientas de IA organizadas por categoría.</p>",
    unsafe_allow_html=True,
)
st.markdown("---")


# ── SECCIÓN 1: Predicción y Series de Tiempo ──────────────────────────────────
st.markdown('<div class="section-label">⏱ Predicción y Series de Tiempo</div>',
            unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)

with c1:
    with st.container():
        st.markdown('<div class="app-card">', unsafe_allow_html=True)
        card(
            "⚡ Sol Energy Forecast",
            "Energy_forecast.png",
            "Predicción de energía solar mediante redes LSTM. Visualiza tendencias y proyecciones en tiempo real.",
            "https://solenergyforecast.streamlit.app/",
            "LSTM"
        )
        st.markdown('</div>', unsafe_allow_html=True)

with c2:
    with st.container():
        st.markdown('<div class="app-card">', unsafe_allow_html=True)
        card(
            "📝 Generador de Texto LSTM",
            "OIG5.jpg",
            "Genera texto coherente entrenado con LSTM. Escribe una semilla y observa cómo la IA continúa la historia.",
            "https://textgeneratoor.streamlit.app/",
            "LSTM"
        )
        st.markdown('</div>', unsafe_allow_html=True)

with c3:
    with st.container():
        st.markdown('<div class="app-card">', unsafe_allow_html=True)
        card(
            "🧠 Red Neuronal Básica",
            "OIG8.jpg",
            "Explora cómo una RNN predice secuencias temporales. Ajusta parámetros y ve los resultados al instante.",
            "https://rnnbasica.streamlit.app/",
            "RNN"
        )
        st.markdown('</div>', unsafe_allow_html=True)

with c4:
    with st.container():
        st.markdown('<div class="app-card">', unsafe_allow_html=True)
        card(
            "🎲 Autoencoder Variacional",
            "Chat_pdf.png",
            "Genera y explora dígitos con un VAE interactivo. Modifica el espacio latente y crea nuevas imágenes.",
            "https://aevminists.streamlit.app/",
            "VAE"
        )
        st.markdown('</div>', unsafe_allow_html=True)


# ── SECCIÓN 2: Visión por Computadora ────────────────────────────────────────
st.markdown('<div class="section-label">👁 Visión por Computadora</div>',
            unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)

with c1:
    with st.container():
        st.markdown('<div class="app-card">', unsafe_allow_html=True)
        card(
            "🌸 Clasificador de Flores",
            "OIG5.jpg",
            "Sube una foto y la IA identifica la especie de flor. Modelo de clasificación entrenado con Transfer Learning.",
            "https://tlflores.streamlit.app/",
            "CNN"
        )
        st.markdown('</div>', unsafe_allow_html=True)

with c2:
    with st.container():
        st.markdown('<div class="app-card">', unsafe_allow_html=True)
        card(
            "🐶 YOGI · Reconocimiento de Imágenes",
            "OIG5.jpg",
            "Clasifica imágenes con tu modelo de Teachable Machine. Apunta la cámara y obtén predicciones al instante.",
            "https://teachablem-yogi.streamlit.app/",
            "Teachable"
        )
        st.markdown('</div>', unsafe_allow_html=True)

with c3:
    with st.container():
        st.markdown('<div class="app-card">', unsafe_allow_html=True)
        card(
            "🔍 Detección de Objetos YOLO",
            "OIG4.jpg",
            "Detecta y etiqueta objetos en imágenes usando YOLOv5. Alta precisión en tiempo real con bounding boxes.",
            "https://yolov55.streamlit.app/",
            "YOLO"
        )
        st.markdown('</div>', unsafe_allow_html=True)

with c4:
    with st.container():
        st.markdown('<div class="app-card">', unsafe_allow_html=True)
        card(
            "✍️ Detector de Dígitos",
            "OIG4.jpg",
            "Dibuja un número y la red neuronal lo reconoce al instante. Modelo entrenado sobre el dataset MNIST.",
            "https://hzwi7bwfepy6scpu7pradh.streamlit.app/",
            "CNN"
        )
        st.markdown('</div>', unsafe_allow_html=True)


# ── SECCIÓN 3: Procesamiento de Lenguaje ─────────────────────────────────────
st.markdown('<div class="section-label">💬 Procesamiento de Lenguaje</div>',
            unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)

with c1:
    with st.container():
        st.markdown('<div class="app-card">', unsafe_allow_html=True)
        card(
            "🌐 Traductor IA",
            "OIG5.jpg",
            "Traduce textos entre múltiples idiomas usando modelos de NLP. Rápido, preciso y con soporte multilingüe.",
            "https://traductore.streamlit.app/",
            "NLP"
        )
        st.markdown('</div>', unsafe_allow_html=True)

with c2:
    with st.container():
        st.markdown('<div class="app-card">', unsafe_allow_html=True)
        card(
            "❤️ Análisis de Sentimiento",
            "txt_to_audio.png",
            "Analiza el tono emocional de cualquier texto: positivo, negativo o neutro. Ideal para reseñas y encuestas.",
            "https://sentimientos-1.streamlit.app/",
            "NLP"
        )
        st.markdown('</div>', unsafe_allow_html=True)

with c3:
    with st.container():
        st.markdown('<div class="app-card">', unsafe_allow_html=True)
        card(
            "🔊 Text to Speech",
            "txt_to_audio2.png",
            "Convierte cualquier texto en audio natural. Elige idioma y voz, descarga el resultado en segundos.",
            "https://text-to-voic.streamlit.app/",
            "TTS"
        )
        st.markdown('</div>', unsafe_allow_html=True)

with c4:
    with st.container():
        st.markdown('<div class="app-card">', unsafe_allow_html=True)
        card(
            "☁️ Nube de Palabras",
            "OIG5.jpg",
            "Visualiza las palabras más frecuentes en cualquier texto. Explora cómo funciona la IA generativa.",
            "https://wordcloud-1.streamlit.app/",
            "NLP"
        )
        st.markdown('</div>', unsafe_allow_html=True)


# ── SECCIÓN 4: OCR y Documentos ──────────────────────────────────────────────
st.markdown('<div class="section-label">📄 OCR y Documentos</div>',
            unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)

with c1:
    with st.container():
        st.markdown('<div class="app-card">', unsafe_allow_html=True)
        card(
            "🔡 OCR a Audio",
            "OIG3.jpg",
            "Extrae texto de imágenes con OCR y lo convierte en audio. Útil para documentos físicos o capturas de pantalla.",
            "https://ocr-audioo.streamlit.app/",
            "OCR"
        )
        st.markdown('</div>', unsafe_allow_html=True)

with c2:
    with st.container():
        st.markdown('<div class="app-card">', unsafe_allow_html=True)
        card(
            "📑 OCR Avanzado",
            "Chat_pdf.png",
            "Reconocimiento óptico de caracteres sobre documentos complejos. Extrae, estructura y exporta el contenido.",
            "https://opticalcr.streamlit.app/",
            "OCR"
        )
        st.markdown('</div>', unsafe_allow_html=True)

with c3:
    with st.container():
        st.markdown('<div class="app-card">', unsafe_allow_html=True)
        card(
            "📚 RAG · Chat con PDF",
            "Chat_pdf.png",
            "Carga un PDF y hazle preguntas. Usa Recuperación Aumentada (RAG) para respuestas precisas sobre el documento.",
            "https://chatpdefe.streamlit.app/",
            "RAG"
        )
        st.markdown('</div>', unsafe_allow_html=True)

with c4:
    with st.container():
        st.markdown('<div class="app-card">', unsafe_allow_html=True)
        card(
            "📊 Análisis de Datos con Agentes",
            "data_analisis.png",
            "Sube tus datos y deja que un agente de IA los explore, limpie y genere visualizaciones automáticamente.",
            "https://dataagentt.streamlit.app/",
            "Agentes"
        )
        st.markdown('</div>', unsafe_allow_html=True)


# ── SECCIÓN 5: Sistemas y Redes Avanzadas ────────────────────────────────────
st.markdown('<div class="section-label">⚙️ Sistemas y Redes Avanzadas</div>',
            unsafe_allow_html=True)
c1, c2, c3, _ = st.columns(4)

with c1:
    with st.container():
        st.markdown('<div class="app-card">', unsafe_allow_html=True)
        card(
            "🎛 Convoluciones Interactivas",
            "OIG6.jpg",
            "Aplica filtros convolucionales a imágenes en vivo. Visualiza cómo las CNN procesan bordes y texturas.",
            "https://convoluciones.streamlit.app/",
            "CNN"
        )
        st.markdown('</div>', unsafe_allow_html=True)

with c2:
    with st.container():
        st.markdown('<div class="app-card">', unsafe_allow_html=True)
        card(
            "🌐 Sistema Ciberfísico · GPT",
            "Chat_pdf.png",
            "Interactúa con el mundo físico a través de ChatGPT. Conecta IA con sensores y dispositivos reales.",
            "https://chatgptexploring.streamlit.app/",
            "ChatGPT"
        )
        st.markdown('</div>', unsafe_allow_html=True)

with c3:
    with st.container():
        st.markdown('<div class="app-card">', unsafe_allow_html=True)
        card(
            "🔮 Sistema Ciberfísico · Anthropic",
            "OIG6.jpg",
            "Versión del sistema ciberfísico usando Claude de Anthropic. Mayor contexto y razonamiento complejo.",
            "https://chatbot-antropic.streamlit.app/",
            "Claude"
        )
        st.markdown('</div>', unsafe_allow_html=True)

with _:
    with st.container():
        st.markdown('<div class="app-card">', unsafe_allow_html=True)
        card(
            "🏞️ Análisis de Imagen",
            "OIG5.jpg",
            "Describe y analiza el contenido de cualquier imagen con visión artificial. Detecta objetos, escenas y más.",
            "https://visionn.streamlit.app/",
            "Visión"
        )
        st.markdown('</div>', unsafe_allow_html=True)
