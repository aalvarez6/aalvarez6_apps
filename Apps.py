import streamlit as st
from PIL import Image
import base64

st.set_page_config(layout="wide")

# -------------------- GLOBAL STYLE --------------------
st.markdown("""
<style>

/* Fondo con estrellas */
.stApp {
  background: #020617;
  color: white;
  overflow-x: hidden;
}

/* estrellas animadas */
.stApp::before {
  content: "";
  position: fixed;
  width: 200%;
  height: 200%;
  top: -50%;
  left: -50%;
  background-image: radial-gradient(white 1px, transparent 1px);
  background-size: 40px 40px;
  opacity: 0.08;
  animation: starsMove 80s linear infinite;
  z-index: -1;
}

@keyframes starsMove {
  from { transform: translate(0,0); }
  to { transform: translate(200px, 300px); }
}

/* Layout */
.block-container {
  max-width: 1200px;
}

/* Cards */
.card {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 16px;
  padding: 14px;
  transition: 0.3s;
  height: 100%;
}

.card:hover {
  transform: translateY(-6px);
  border: 1px solid #7c3aed;
  box-shadow: 0 10px 30px rgba(124,58,237,0.3);
}

/* Imagen uniforme */
.card-img {
  width: 100%;
  height: 180px;
  object-fit: cover;
  border-radius: 10px;
  margin-bottom: 10px;
}

/* Texto */
.card-title {
  font-size:17px;
  font-weight:600;
}

.card-desc {
  font-size:13px;
  color:#a1a1aa;
  margin:6px 0;
}

.card a {
  color:#c084fc;
  text-decoration:none;
  font-size:13px;
}

/* Header */
.title {
  font-size:60px;
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

# -------------------- SPACE HERO --------------------
st.components.v1.html("""
<canvas id="space"></canvas>

<script>
const canvas = document.getElementById("space");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth * 0.9;
canvas.height = 180;

let t = 0;

const earth = {x: 80, y: 120, r: 30};
const moon = {x: canvas.width - 80, y: 60, r: 15};

function drawPlanet(p, color){
  ctx.beginPath();
  ctx.arc(p.x, p.y, p.r, 0, Math.PI*2);
  ctx.fillStyle = color;
  ctx.fill();
}

function drawRocket(x,y){
  ctx.save();
  ctx.translate(x,y);

  ctx.fillStyle = "#c084fc";

  ctx.beginPath();
  ctx.moveTo(0,-10);
  ctx.lineTo(6,10);
  ctx.lineTo(-6,10);
  ctx.closePath();
  ctx.fill();

  ctx.beginPath();
  ctx.moveTo(-3,10);
  ctx.lineTo(3,10);
  ctx.lineTo(0,18 + Math.sin(t*5)*4);
  ctx.fillStyle = "#f97316";
  ctx.fill();

  ctx.restore();
}

function animate(){

  ctx.fillStyle="#020617";
  ctx.fillRect(0,0,canvas.width,canvas.height);

  drawPlanet(earth,"#2563eb");
  drawPlanet(moon,"#a1a1aa");

  let progress = (Math.sin(t)+1)/2;
  let x = earth.x + (moon.x - earth.x) * progress;
  let y = earth.y - 80*Math.sin(progress*Math.PI);

  drawRocket(x,y);

  t += 0.02;
  requestAnimationFrame(animate);
}

animate();
</script>
""", height=200)

# -------------------- HEADER --------------------
st.markdown('<div class="title">Artemis Hub</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI Applications Platform</div>', unsafe_allow_html=True)

# -------------------- DATA --------------------
apps = [
    {"name":"Energy Forecast","desc":"LSTM solar predictions","url":"https://solenergyforecast.streamlit.app/","img":"renewable-energy-forecast-solar-wind-infographic-1024x683.webp"},
    {"name":"Flower Classifier","desc":"Image classification model","url":"https://tlflores.streamlit.app/","img":"photo_9_2026-03-17_16-25-34.jpg"},
    {"name":"Translator","desc":"Multi-language AI translator","url":"https://traductore.streamlit.app/","img":"OIG5.jpg"},
    {"name":"Image Analysis","desc":"Describe images with AI","url":"https://visionn.streamlit.app/","img":"OIG5.jpg"},
    {"name":"Wordcloud","desc":"Text visualization","url":"https://wordcloud-1.streamlit.app/","img":"OIG5.jpg"},
    {"name":"Text Generator","desc":"LSTM generation","url":"https://textgeneratoor.streamlit.app/","img":"OIG5.jpg"},
    {"name":"Sentiment Analysis","desc":"Detect emotions","url":"https://sentimientos-1.streamlit.app/","img":"txt_to_audio.png"},
    {"name":"Neural Network","desc":"Time series prediction","url":"https://rnnbasica.streamlit.app/","img":"OIG8.jpg"},
    {"name":"OCR to Audio","desc":"Text to audio","url":"https://ocr-audioo.streamlit.app/","img":"OIG3.jpg"},
    {"name":"Advanced OCR","desc":"Document recognition","url":"https://opticalcr.streamlit.app/","img":"Chat_pdf.png"},
    {"name":"Text to Speech","desc":"Speech synthesis","url":"https://text-to-voic.streamlit.app/","img":"txt_to_audio2.png"},
    {"name":"Object Detection","desc":"YOLO detection","url":"https://yolov55.streamlit.app/","img":"OIG4.jpg"},
    {"name":"Data Analysis","desc":"AI data agent","url":"https://dataagentt.streamlit.app/","img":"data_analisis.png"},
    {"name":"RAG with PDF","desc":"Ask documents","url":"https://chatpdefe.streamlit.app/","img":"Chat_pdf.png"},
]

# -------------------- IMAGE HELPER --------------------
def get_base64(img_path):
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# -------------------- GRID --------------------
cols = st.columns(3)

for i, app in enumerate(apps):
    col = cols[i % 3]

    with col:
        try:
            img_base64 = get_base64(app["img"])
            st.markdown(f"""
            <img src="data:image/png;base64,{img_base64}" class="card-img">
            """, unsafe_allow_html=True)
        except:
            pass

        st.markdown(f"""
        <div class="card">
            <div class="card-title">{app['name']}</div>
            <div class="card-desc">{app['desc']}</div>
            <a href="{app['url']}" target="_blank">Open App →</a>
        </div>
        """, unsafe_allow_html=True)
