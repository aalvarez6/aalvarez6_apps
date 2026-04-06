import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

# -------------------- STYLE --------------------
st.markdown("""
<style>

/* Fondo */
.stApp {
  background: #020617;
  color: white;
}

/* Estrellas */
.stApp::before {
  content: "";
  position: fixed;
  width: 200%;
  height: 200%;
  background-image: radial-gradient(white 1px, transparent 1px);
  background-size: 40px 40px;
  opacity: 0.08;
  animation: moveStars 80s linear infinite;
  z-index: -1;
}

@keyframes moveStars {
  from { transform: translate(0,0); }
  to { transform: translate(200px,300px); }
}

/* Layout */
.block-container {
  max-width: 1000px;
}

/* Cards */
.card {
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 14px;
  padding: 10px;
  transition: 0.25s;
}

.card:hover {
  transform: translateY(-4px);
  border: 1px solid #7c3aed;
}

/* Imagen */
.card img {
  width: 100%;
  height: 130px;
  object-fit: cover;
  border-radius: 10px;
  margin-bottom: 6px;
}

/* Texto */
.card-title {
  font-size:15px;
  font-weight:600;
}

.card-desc {
  font-size:12px;
  color:#a1a1aa;
  margin:4px 0;
}

.card a {
  color:#c084fc;
  font-size:12px;
  text-decoration:none;
}

/* Header */
.title {
  font-size:52px;
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
<canvas id="spaceCanvas"></canvas>

<script>
const canvas = document.getElementById("spaceCanvas");
const ctx = canvas.getContext("2d");

canvas.width = 1000;
canvas.height = 180;

let t = 0;

const earth = {x: 80, y: 130, r: 25};
const moon = {x: 920, y: 60, r: 12};

function drawPlanet(p, color){
  ctx.beginPath();
  ctx.arc(p.x, p.y, p.r, 0, Math.PI*2);
  ctx.fillStyle = color;
  ctx.fill();
}

function drawRocket(x, y){
  ctx.save();
  ctx.translate(x, y);

  ctx.fillStyle = "#c084fc";
  ctx.beginPath();
  ctx.moveTo(0, -12);
  ctx.lineTo(8, 10);
  ctx.lineTo(-8, 10);
  ctx.closePath();
  ctx.fill();

  ctx.beginPath();
  ctx.arc(0, -2, 3, 0, Math.PI*2);
  ctx.fillStyle = "#1e1b4b";
  ctx.fill();

  ctx.beginPath();
  ctx.moveTo(-4,10);
  ctx.lineTo(4,10);
  ctx.lineTo(0, 20 + Math.sin(t*6)*5);
  ctx.fillStyle = "#f97316";
  ctx.fill();

  ctx.restore();
}

function animate(){
  ctx.fillStyle = "#020617";
  ctx.fillRect(0,0,canvas.width,canvas.height);

  drawPlanet(earth,"#2563eb");
  drawPlanet(moon,"#a1a1aa");

  let progress = (Math.sin(t)+1)/2;
  let x = earth.x + (moon.x - earth.x) * progress;
  let y = earth.y - 80 * Math.sin(progress * Math.PI);

  drawRocket(x,y);

  t += 0.03;
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
    {"name":"Flower Classifier","desc":"Image classification","url":"https://tlflores.streamlit.app/","img":"photo_9_2026-03-17_16-25-34.jpg"},
    {"name":"Translator","desc":"AI translator","url":"https://traductore.streamlit.app/","img":"OIG5.jpg"},
    {"name":"Image Analysis","desc":"Describe images","url":"https://visionn.streamlit.app/","img":"OIG5.jpg"},
    {"name":"Wordcloud","desc":"Text visualization","url":"https://wordcloud-1.streamlit.app/","img":"OIG5.jpg"},
    {"name":"Text Generator","desc":"Generate text","url":"https://textgeneratoor.streamlit.app/","img":"OIG5.jpg"},
    {"name":"Sentiment Analysis","desc":"Detect emotions","url":"https://sentimientos-1.streamlit.app/","img":"txt_to_audio.png"},
    {"name":"Neural Network","desc":"Time series","url":"https://rnnbasica.streamlit.app/","img":"OIG8.jpg"},
    {"name":"OCR to Audio","desc":"Text to speech","url":"https://ocr-audioo.streamlit.app/","img":"OIG3.jpg"},
    {"name":"Advanced OCR","desc":"Document AI","url":"https://opticalcr.streamlit.app/","img":"Chat_pdf.png"},
    {"name":"Text to Speech","desc":"Speech synthesis","url":"https://text-to-voic.streamlit.app/","img":"txt_to_audio2.png"},
    {"name":"Object Detection","desc":"YOLO detection","url":"https://yolov55.streamlit.app/","img":"OIG4.jpg"},
    {"name":"Data Analysis","desc":"AI data agent","url":"https://dataagentt.streamlit.app/","img":"data_analisis.png"},
    {"name":"RAG with PDF","desc":"Chat with docs","url":"https://chatpdefe.streamlit.app/","img":"Chat_pdf.png"},
]

# -------------------- GRID --------------------
cols = st.columns(4)

for i, app in enumerate(apps):
    col = cols[i % 4]

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
