import streamlit as st
from PIL import Image


st.markdown("""
<style>
/* Fondo global */
.stApp {
  background: radial-gradient(circle at 20% 20%, #1e1b4b, #020617 60%);
  color: white;
  overflow-x: hidden;
}

/* estrellas */
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
  animation: starsMove 60s linear infinite;
  z-index: -1;
}

@keyframes starsMove {
  from { transform: translate(0,0); }
  to { transform: translate(100px, 200px); }
}
</style>
""", unsafe_allow_html=True)

# Logo
st.components.v1.html("""
<style>
.hero {
  display:flex;
  flex-direction:column;
  align-items:center;
  text-align:center;
  padding:50px 20px;
}

h1 {
  font-size:52px;
  font-weight:900;
  margin:10px 0;
  background: linear-gradient(90deg, #c084fc, #7c3aed);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.tagline {
  color:#a78bfa;
  font-size:14px;
  letter-spacing:2px;
}

.desc {
  color:#94a3b8;
  font-size:16px;
  max-width:600px;
}

canvas {
  margin-bottom:20px;
}
</style>

<div class="hero">
  <canvas id="c" width="320" height="160"></canvas>

  <h1>AleAI</h1>

  <div class="tagline">
    INTELLIGENCE THAT BUILDS.
  </div>

  <div class="desc">
    Distributed AI systems inspired by nature — optimizing, learning, 
    and building solutions collectively.
  </div>
</div>

<script>
const canvas = document.getElementById("c");
const ctx = canvas.getContext("2d");

let ants = [];
const N = 12;

// Crear hormigas
for (let i = 0; i < N; i++) {
  ants.push({
    x: Math.random() * canvas.width,
    y: canvas.height/2 + Math.random()*40,
    vx: (Math.random() - 0.5) * 1.5,
    vy: (Math.random() - 0.5) * 1.5
  });
}

let t = 0;

function drawAnt(a) {
  ctx.save();
  ctx.translate(a.x, a.y);

  // cuerpo (3 partes)
  ctx.fillStyle = "#7c3aed";

  ctx.beginPath(); ctx.arc(0,0,4,0,Math.PI*2); ctx.fill();
  ctx.beginPath(); ctx.arc(-6,0,3,0,Math.PI*2); ctx.fill();
  ctx.beginPath(); ctx.arc(6,0,3,0,Math.PI*2); ctx.fill();

  // patas
  ctx.strokeStyle = "#a78bfa";
  ctx.lineWidth = 1;

  for (let i=-1;i<=1;i++){
    ctx.beginPath();
    ctx.moveTo(0,0);
    ctx.lineTo(8, i*4);
    ctx.stroke();
  }

  ctx.restore();
}

function drawTunnel() {
  ctx.beginPath();
  ctx.moveTo(0, canvas.height/2 + 30);

  for (let x = 0; x < canvas.width; x+=10){
    let y = canvas.height/2 + 30 + Math.sin(x*0.05 + t)*5;
    ctx.lineTo(x,y);
  }

  ctx.strokeStyle = "#312e81";
  ctx.lineWidth = 3;
  ctx.stroke();
}

function update() {
  ctx.clearRect(0,0,canvas.width,canvas.height);

  drawTunnel();

  ants.forEach(a => {
    a.x += a.vx;
    a.y += a.vy + Math.sin(t)*0.2;

    // límites
    if (a.x < 0 || a.x > canvas.width) a.vx *= -1;
    if (a.y < canvas.height/2 || a.y > canvas.height) a.vy *= -1;

    drawAnt(a);
  });

  t += 0.03;
  requestAnimationFrame(update);
}

update();
</script>
""", height=420)

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.write(f"Link to pages and exercises: [Link]({url_ia})")

col1, col2, col3, col4 = st.columns(4, gap="small")

with col1:

  st.subheader(" Energy Forecast  ")
  image = Image.open('renewable-energy-forecast-solar-wind-infographic-1024x683.webp')
  st.image(image, width=200)
  st.write("LSTM predictions for solar energy generation in real time.")
  url = "https://solenergyforecast.streamlit.app/"
  st.write(f"Sol Energy Forecast: [Link]({url})")

  st.subheader("       Flower Classifier     ")
  image = Image.open('photo_9_2026-03-17_16-25-34.jpg')
  st.image(image, width=200)
  st.write("Classify flower species using your own trained model.")
  url = "https://tlflores.streamlit.app/"
  st.write(f"Flower Classifier: [Link]({url})")

  st.subheader(" Translator            ")
  image = Image.open('OIG5.jpg')
  st.image(image, width=200)
  st.write("AI-powered translation app supporting multiple languages.")
  url = "https://traductore.streamlit.app/"
  st.write(f"Translator: [Link]({url})")

  st.subheader(" Image Analysis        ")
  image = Image.open('OIG5.jpg')
  st.image(image, width=200)
  st.write("Analyze and describe the content of any image with AI.")
  url = "https://visionn.streamlit.app/"
  st.write(f"Image Analysis: [Link]({url})")

  st.subheader(" Wordcloud             ")
  image = Image.open('OIG5.jpg')
  st.image(image, width=200)
  st.write("Visualize the most frequent words in any text with AI.")
  url = "https://wordcloud-1.streamlit.app/"
  st.write(f"Wordcloud: [Link]({url})")


with col2:

  st.subheader(" Text Generator   ")
  image = Image.open('OIG5.jpg')
  st.image(image, width=200)
  st.write("Generate coherent text using an LSTM neural network model.")
  url = "https://textgeneratoor.streamlit.app/"
  st.write(f"LSTM Text Generator: [Link]({url})")

  st.subheader(" YOGI    ")
  image = Image.open('OIG5.jpg')
  st.image(image, width=200)
  st.write("Use your Teachable Machine model for image recognition.")
  url = "https://teachablem-yogi.streamlit.app/"
  st.write(f"YOGI: [Link]({url})")

  st.subheader(" Sentiment Analysis    ")
  image = Image.open('txt_to_audio.png')
  st.image(image, width=200)
  st.write("Detect positive, negative or neutral tone in any text.")
  url = "https://sentimientos-1.streamlit.app/"
  st.write(f"Sentiment Analysis: [Link]({url})")

  st.subheader(" Neural Network  ")
  image = Image.open('OIG8.jpg')
  st.image(image, width=200)
  st.write("RNN application for time series sequence prediction.")
  url = "https://rnnbasica.streamlit.app/"
  st.write(f"Basic Neural Network: [Link]({url})")

  st.subheader(" OCR to Audio          ")
  image = Image.open('OIG3.jpg')
  st.image(image, width=200)
  st.write("Extract text from images using OCR and convert to audio.")
  url = "https://ocr-audioo.streamlit.app/"
  st.write(f"OCR to Audio: [Link]({url})")


with col3:

  st.subheader(" Advanced OCR          ")
  image = Image.open('Chat_pdf.png')
  st.image(image, width=200)
  st.write("Advanced optical character recognition on complex documents.")
  url = "https://opticalcr.streamlit.app/"
  st.write(f"Advanced OCR: [Link]({url})")

  st.subheader("Handwritten Digits ")
  image = Image.open('OIG4.jpg')
  st.image(image, width=200)
  st.write("Draw a digit and the neural network recognizes it instantly.")
  url = "https://hzwi7bwfepy6scpu7pradh.streamlit.app/"
  st.write(f"Handwritten Digits: [Link]({url})")

  st.subheader(" Text to Speech        ")
  image = Image.open('txt_to_audio2.png')
  st.image(image, width=200)
  st.write("Convert any text into natural speech audio with AI.")
  url = "https://text-to-voic.streamlit.app/"
  st.write(f"Text to Speech: [Link]({url})")

  st.subheader(" Object Detection      ")
  image = Image.open('OIG4.jpg')
  st.image(image, width=200)
  st.write("Detect and label objects in images using YOLOv5 in real time.")
  url = "https://yolov55.streamlit.app/"
  st.write(f"Object Detection: [Link]({url})")

  st.subheader(" Data Analysis         ")
  image = Image.open('data_analisis.png')
  st.image(image, width=200)
  st.write("AI agents explore, clean and visualize your data automatically.")
  url = "https://dataagentt.streamlit.app/"
  st.write(f"Data Analysis: [Link]({url})")


with col4:

  st.subheader(" Convolutions")
  image = Image.open('OIG6.jpg')
  st.image(image, width=200)
  st.write("Explore how convolutional filters transform images live.")
  url = "https://convoluciones.streamlit.app/"
  st.write(f"Convolutions: [Link]({url})")

  st.subheader(" Cyber-Physical")
  image = Image.open('Chat_pdf.png')
  st.image(image, width=200)
  st.write("Interact with the physical world using ChatGPT as the AI engine.")
  url = "https://chatgptexploring.streamlit.app/"
  st.write(f"Cyber-Physical GPT: [Link]({url})")

  st.subheader(" Cyber-Physical")
  image = Image.open('OIG6.jpg')
  st.image(image, width=200)
  st.write("Cyber-physical interaction powered by Anthropic's Claude model.")
  url = "https://chatbot-antropic.streamlit.app/"
  st.write(f"Cyber-Physical Claude: [Link]({url})")

  st.subheader(" RAG with PDF          ")
  image = Image.open('Chat_pdf.png')
  st.image(image, width=200)
  st.write("Upload a PDF and ask questions using Retrieval-Augmented Generation.")
  url = "https://chatpdefe.streamlit.app/"
  st.write(f"RAG with PDF: [Link]({url})")

  st.subheader(" Interactive Autoencoder")
  image = Image.open('Chat_pdf.png')
  st.image(image, width=200)
  st.write("Explore and generate digits with an interactive Variational Autoencoder.")
  url = "https://aevminists.streamlit.app/"
  st.write(f"Autoencoder: [Link]({url})")
