import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

# -------------------- STYLE --------------------
st.markdown("""
<style>

/* Fondo */
.stApp {
  background: radial-gradient(circle at 50% 0%, #0f0f1a, #020617 60%);
  color: white;
}

/* Layout */
.block-container {
  max-width: 1200px;
  padding-top: 2rem;
}

/* Cards */
.card {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 16px;
  padding: 16px;
  transition: 0.3s;
}

.card:hover {
  transform: translateY(-6px);
  border: 1px solid #7c3aed;
  box-shadow: 0 10px 30px rgba(124,58,237,0.3);
}

/* Titles */
.card-title {
  font-size:18px;
  font-weight:600;
  margin-bottom:6px;
}

/* Description */
.card-desc {
  font-size:14px;
  color:#a1a1aa;
  margin-bottom:10px;
}

/* Button link */
.card a {
  color:#c084fc;
  text-decoration:none;
  font-size:14px;
}

/* Filters */
.filter-bar {
  margin:20px 0;
}

/* Header */
.title {
  font-size:56px;
  font-weight:900;
  text-align:center;
  background: linear-gradient(90deg, #c084fc, #7c3aed);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.subtitle {
  text-align:center;
  color:#a1a1aa;
  margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# -------------------- HEADER --------------------
st.markdown('<div class="title">Artemis Hub</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI Applications Platform</div>', unsafe_allow_html=True)

# -------------------- DATA --------------------
apps = [
    {"name":"Energy Forecast","desc":"LSTM solar predictions","url":"https://solenergyforecast.streamlit.app/","img":"renewable-energy-forecast-solar-wind-infographic-1024x683.webp","cat":"Forecasting"},
    {"name":"Flower Classifier","desc":"Image classification model","url":"https://tlflores.streamlit.app/","img":"photo_9_2026-03-17_16-25-34.jpg","cat":"Vision"},
    {"name":"Translator","desc":"Multi-language AI translator","url":"https://traductore.streamlit.app/","img":"OIG5.jpg","cat":"Language"},
    {"name":"Image Analysis","desc":"Describe images with AI","url":"https://visionn.streamlit.app/","img":"OIG5.jpg","cat":"Vision"},
    {"name":"Wordcloud","desc":"Text frequency visualization","url":"https://wordcloud-1.streamlit.app/","img":"OIG5.jpg","cat":"Data"},
    {"name":"Text Generator","desc":"LSTM text generation","url":"https://textgeneratoor.streamlit.app/","img":"OIG5.jpg","cat":"Language"},
    {"name":"Sentiment Analysis","desc":"Detect emotions in text","url":"https://sentimientos-1.streamlit.app/","img":"txt_to_audio.png","cat":"Language"},
    {"name":"Neural Network","desc":"Time series prediction","url":"https://rnnbasica.streamlit.app/","img":"OIG8.jpg","cat":"Forecasting"},
    {"name":"OCR to Audio","desc":"Extract text and convert to audio","url":"https://ocr-audioo.streamlit.app/","img":"OIG3.jpg","cat":"Vision"},
    {"name":"Advanced OCR","desc":"Complex document recognition","url":"https://opticalcr.streamlit.app/","img":"Chat_pdf.png","cat":"Vision"},
    {"name":"Text to Speech","desc":"Convert text into audio","url":"https://text-to-voic.streamlit.app/","img":"txt_to_audio2.png","cat":"Language"},
    {"name":"Object Detection","desc":"YOLOv5 detection","url":"https://yolov55.streamlit.app/","img":"OIG4.jpg","cat":"Vision"},
    {"name":"Data Analysis","desc":"AI data exploration","url":"https://dataagentt.streamlit.app/","img":"data_analisis.png","cat":"Data"},
    {"name":"RAG with PDF","desc":"Ask questions to documents","url":"https://chatpdefe.streamlit.app/","img":"Chat_pdf.png","cat":"Data"},
]

# -------------------- FILTERS --------------------
categories = ["All"] + sorted(list(set([a["cat"] for a in apps])))

col1, col2 = st.columns([2,1])

with col1:
    search = st.text_input("🔍 Search apps")

with col2:
    selected_cat = st.selectbox("Category", categories)

# -------------------- FILTER LOGIC --------------------
filtered_apps = []
for app in apps:
    if (selected_cat == "All" or app["cat"] == selected_cat):
        if search.lower() in app["name"].lower():
            filtered_apps.append(app)

# -------------------- GRID --------------------
cols = st.columns(3)

for i, app in enumerate(filtered_apps):
    col = cols[i % 3]
    
    with col:
        try:
            img = Image.open(app["img"])
            st.image(img, use_column_width=True)
        except:
            pass
        
        st.markdown(f"""
        <div class="card">
            <div class="card-title">{app['name']}</div>
            <div class="card-desc">{app['desc']}</div>
            <a href="{app['url']}" target="_blank">Open App →</a>
        </div>
        """, unsafe_allow_html=True)
