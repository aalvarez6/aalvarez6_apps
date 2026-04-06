import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

# ==============================================================
# IMAGES — place these files in the same folder as app.py
# --------------------------------------------------------------
# img_solar.png          → Sol Energy Forecast
# img_flowers.jpg        → Flower Classifier
# img_translator.jpg     → Translator
# img_vision.jpg         → Image Analysis
# img_wordcloud.jpg      → Wordcloud
# img_textgen.jpg        → LSTM Text Generator
# img_yogi.jpg           → YOGI Image Recognition
# img_sentiment.png      → Sentiment Analysis
# img_rnn.jpg            → Basic Neural Network
# img_ocr_audio.jpg      → OCR to Audio
# img_ocr_doc.png        → Advanced OCR
# img_digits.jpg         → Handwritten Digit Detector
# img_tts.png            → Text to Speech
# img_yolo.jpg           → Object Detection
# img_data.png           → Data Analysis
# img_conv.jpg           → Convolutions
# img_cybergpt.png       → Cyber-Physical GPT
# img_cyberclaude.jpg    → Cyber-Physical Claude
# img_rag.png            → RAG with PDF
# img_vae.png            → Interactive Autoencoder
# ==============================================================

# ── GLOBAL STYLE ──────────────────────────────────────────────
st.markdown("""
<style>
html, body, [class*="css"] {
  font-family: -apple-system, BlinkMacSystemFont, "San Francisco", "Segoe UI", sans-serif;
}
.stApp { background: #020617; color: white; }
.block-container { max-width: 1400px; padding-top: 0rem; }
[data-testid="stSidebar"] {
  background: rgba(255,255,255,0.03);
  border-right: 1px solid rgba(255,255,255,0.07);
}
[data-testid="stSidebar"] p { color: #a1a1aa; font-size: 0.87rem; line-height: 1.6; }
[data-testid="column"] { padding-left: 5px !important; padding-right: 5px !important; }
[data-testid="stImage"] img {
  width: 100% !important; height: 130px !important;
  object-fit: cover !important; border-radius: 10px !important;
  margin-bottom: 4px !important;
}
h3 {
  color: white !important; font-size: 0.88rem !important;
  font-weight: 600 !important; margin: 6px 0 2px !important;
  letter-spacing: -0.2px !important;
}
p { color: #a1a1aa; font-size: 0.8rem !important; margin: 2px 0 4px !important; }
a { color: #34d399 !important; font-size: 0.78rem !important; text-decoration: none !important; }
a:hover { color: #a78bfa !important; text-decoration: underline !important; }
hr { border-color: rgba(255,255,255,0.05) !important; margin: 8px 0 !important; }
</style>
""", unsafe_allow_html=True)

# ── SIDEBAR ───────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🤖 Artificial Intelligence")
    st.write(
        "AI improves decision-making with data, automates routine tasks, "
        "and provides advanced real-time analysis — greater efficiency "
        "across every field."
    )
    st.markdown("---")
    st.markdown("📚 [Pages & Exercises](https://sites.google.com/view/aplicacionesdeia/inicio)")
    st.markdown("---")
    st.caption("Artemis Hub · v2.0")

# ── ANIMATED LOGO: bioluminescent open-claw bear ──────────────
st.components.v1.html("""
<div style="background:#020617;border-radius:16px;padding:8px 0 0;">
  <canvas id="bc" width="900" height="210"
    style="display:block;margin:0 auto;cursor:crosshair;"></canvas>
  <div style="text-align:center;font-family:-apple-system,BlinkMacSystemFont,sans-serif;
    font-size:11px;font-weight:600;letter-spacing:0.22em;text-transform:uppercase;
    color:#34d399;opacity:0.7;padding:4px 0 12px;">AI Applications Platform</div>
</div>
<script>
const cv=document.getElementById('bc');
const cx=cv.getContext('2d');
const W=cv.width,H=cv.height;
let mouse={x:W/2,y:H/2};
cv.addEventListener('mousemove',e=>{
  const r=cv.getBoundingClientRect();
  mouse.x=(e.clientX-r.left)*(W/r.width);
  mouse.y=(e.clientY-r.top)*(H/r.height);
});
let t=0;

const STARS=Array.from({length:100},()=>({
  x:Math.random()*W,y:Math.random()*H,
  r:Math.random()*1.3+0.2,a:Math.random()*0.7+0.2,
  va:(Math.random()-0.5)*0.01
}));
const PART=Array.from({length:45},()=>({
  x:Math.random()*W,y:Math.random()*H,
  vx:(Math.random()-0.5)*0.55,vy:(Math.random()-0.5)*0.55,
  r:Math.random()*2.2+0.6,
  c:['52,211,153','167,139,250','56,189,248'][Math.floor(Math.random()*3)],
  a:Math.random()*0.5+0.25
}));

function drawStars(){
  STARS.forEach(s=>{
    s.a+=s.va;if(s.a>0.9||s.a<0.1)s.va*=-1;
    cx.beginPath();cx.arc(s.x,s.y,s.r,0,Math.PI*2);
    cx.fillStyle=`rgba(255,255,255,${s.a})`;cx.fill();
  });
}

function drawParticles(bx,by){
  PART.forEach(p=>{
    p.x+=p.vx;p.y+=p.vy;
    if(p.x<0)p.x=W;if(p.x>W)p.x=0;
    if(p.y<0)p.y=H;if(p.y>H)p.y=0;
    const dx=bx-p.x,dy=by-p.y,d=Math.sqrt(dx*dx+dy*dy);
    if(d<160&&d>30){p.vx+=dx/d*0.012;p.vy+=dy/d*0.012;}
    const sp=Math.sqrt(p.vx*p.vx+p.vy*p.vy);
    if(sp>1.1){p.vx*=0.93;p.vy*=0.93;}
    cx.beginPath();cx.arc(p.x,p.y,p.r,0,Math.PI*2);
    cx.fillStyle=`rgba(${p.c},${p.a})`;cx.fill();
  });
  for(let i=0;i<PART.length;i++)for(let j=i+1;j<PART.length;j++){
    const dx=PART[i].x-PART[j].x,dy=PART[i].y-PART[j].y,d=Math.sqrt(dx*dx+dy*dy);
    if(d<60){
      cx.beginPath();cx.moveTo(PART[i].x,PART[i].y);cx.lineTo(PART[j].x,PART[j].y);
      cx.strokeStyle=`rgba(52,211,153,${0.12*(1-d/60)})`;cx.lineWidth=0.5;cx.stroke();
    }
  }
}

function drawBear(bx,by){
  const bob=Math.sin(t*1.6)*4;
  const gy=by+bob;
  const pulse=0.7+0.3*Math.sin(t*2.5);
  const pulse2=0.6+0.4*Math.sin(t*2.5+1);

  // aura
  const aura=cx.createRadialGradient(bx,gy,5,bx,gy,100);
  aura.addColorStop(0,'rgba(52,211,153,0.16)');
  aura.addColorStop(0.5,'rgba(56,189,248,0.06)');
  aura.addColorStop(1,'rgba(52,211,153,0)');
  cx.beginPath();cx.arc(bx,gy,100,0,Math.PI*2);cx.fillStyle=aura;cx.fill();

  // LEFT CLAW
  cx.save();cx.translate(bx-58,gy+26);cx.rotate(-0.38+Math.sin(t*1.6)*0.05);
  for(let c=0;c<3;c++){
    const ang=-0.5+c*0.5,len=22+c*3;
    cx.beginPath();cx.moveTo(0,0);
    cx.quadraticCurveTo(Math.cos(ang-0.3)*len*0.6,Math.sin(ang-0.3)*len*0.6-8,Math.cos(ang)*len,Math.sin(ang)*len-10);
    cx.strokeStyle=`rgba(52,211,153,${0.88*pulse})`;cx.lineWidth=3.5;cx.lineCap='round';cx.stroke();
    cx.beginPath();cx.arc(Math.cos(ang)*len,Math.sin(ang)*len-10,3,0,Math.PI*2);
    cx.fillStyle=`rgba(52,211,153,${pulse})`;cx.fill();
  }
  cx.beginPath();cx.ellipse(0,8,10,16,0,0,Math.PI*2);
  const aG=cx.createRadialGradient(0,0,2,0,8,16);
  aG.addColorStop(0,'rgba(56,189,248,0.95)');aG.addColorStop(1,'rgba(13,80,60,0.75)');
  cx.fillStyle=aG;cx.fill();
  cx.strokeStyle=`rgba(52,211,153,${0.65*pulse})`;cx.lineWidth=1.2;cx.stroke();
  cx.restore();

  // RIGHT CLAW
  cx.save();cx.translate(bx+58,gy+26);cx.rotate(0.38+Math.sin(t*1.6+1)*0.05);
  for(let c=0;c<3;c++){
    const ang=Math.PI+0.5-c*0.5,len=22+c*3;
    cx.beginPath();cx.moveTo(0,0);
    cx.quadraticCurveTo(Math.cos(ang+0.3)*len*0.6,Math.sin(ang+0.3)*len*0.6-8,Math.cos(ang)*len,Math.sin(ang)*len-10);
    cx.strokeStyle=`rgba(52,211,153,${0.88*pulse})`;cx.lineWidth=3.5;cx.lineCap='round';cx.stroke();
    cx.beginPath();cx.arc(Math.cos(ang)*len,Math.sin(ang)*len-10,3,0,Math.PI*2);
    cx.fillStyle=`rgba(52,211,153,${pulse})`;cx.fill();
  }
  cx.beginPath();cx.ellipse(0,8,10,16,0,0,Math.PI*2);
  const aG2=cx.createRadialGradient(0,0,2,0,8,16);
  aG2.addColorStop(0,'rgba(56,189,248,0.95)');aG2.addColorStop(1,'rgba(13,80,60,0.75)');
  cx.fillStyle=aG2;cx.fill();
  cx.strokeStyle=`rgba(52,211,153,${0.65*pulse})`;cx.lineWidth=1.2;cx.stroke();
  cx.restore();

  // BODY
  cx.beginPath();cx.ellipse(bx,gy+42,32,30,0,0,Math.PI*2);
  const bG=cx.createRadialGradient(bx-8,gy+30,4,bx,gy+42,34);
  bG.addColorStop(0,'rgba(56,189,248,0.95)');bG.addColorStop(0.5,'rgba(14,116,144,0.85)');bG.addColorStop(1,'rgba(6,50,70,0.9)');
  cx.fillStyle=bG;cx.fill();
  cx.strokeStyle=`rgba(52,211,153,${0.8*pulse})`;cx.lineWidth=1.5;cx.stroke();
  for(let i=0;i<5;i++){
    cx.beginPath();cx.arc(bx-6+i*3,gy+36+i*4,1.2,0,Math.PI*2);
    cx.fillStyle=`rgba(52,211,153,${0.4+0.3*Math.sin(t*3+i)})`;cx.fill();
  }

  // EARS
  [bx-28,bx+28].forEach(ex=>{
    cx.beginPath();cx.arc(ex,gy-44,15,0,Math.PI*2);
    const eG=cx.createRadialGradient(ex,gy-44,2,ex,gy-44,15);
    eG.addColorStop(0,'rgba(56,189,248,0.92)');eG.addColorStop(1,'rgba(6,50,70,0.82)');
    cx.fillStyle=eG;cx.fill();
    cx.strokeStyle=`rgba(52,211,153,${0.7*pulse})`;cx.lineWidth=1.2;cx.stroke();
    cx.beginPath();cx.arc(ex,gy-44,7,0,Math.PI*2);
    cx.fillStyle=`rgba(52,211,153,${0.55*pulse2})`;cx.fill();
  });

  // HEAD
  cx.beginPath();cx.ellipse(bx,gy-14,40,37,0,0,Math.PI*2);
  const hG=cx.createRadialGradient(bx-10,gy-22,4,bx,gy-14,40);
  hG.addColorStop(0,'rgba(56,189,248,0.95)');hG.addColorStop(0.6,'rgba(14,116,144,0.88)');hG.addColorStop(1,'rgba(6,50,70,0.92)');
  cx.fillStyle=hG;cx.fill();
  cx.strokeStyle=`rgba(52,211,153,${0.75*pulse})`;cx.lineWidth=1.5;cx.stroke();

  cx.beginPath();cx.ellipse(bx,gy+2,21,17,0,0,Math.PI*2);
  cx.fillStyle='rgba(56,189,248,0.22)';cx.fill();

  // EYES
  const oX=Math.max(-6,Math.min(6,(mouse.x-bx)*0.08));
  const oY=Math.max(-4,Math.min(4,(mouse.y-gy)*0.06));
  [bx-15,bx+15].forEach(ex=>{
    cx.beginPath();cx.ellipse(ex,gy-20,9,10,0,0,Math.PI*2);
    cx.fillStyle='rgba(220,255,245,0.93)';cx.fill();
    cx.strokeStyle=`rgba(52,211,153,${0.8*pulse})`;cx.lineWidth=1;cx.stroke();
    cx.beginPath();cx.arc(ex+oX,gy-20+oY,4.5,0,Math.PI*2);cx.fillStyle='#050e14';cx.fill();
    cx.beginPath();cx.arc(ex+oX,gy-20+oY,2,0,Math.PI*2);
    cx.fillStyle=`rgba(52,211,153,${0.9*pulse})`;cx.fill();
    cx.beginPath();cx.arc(ex+oX+2,gy-22+oY,1.2,0,Math.PI*2);
    cx.fillStyle='rgba(255,255,255,0.8)';cx.fill();
  });

  // NOSE
  cx.beginPath();cx.ellipse(bx,gy-5,6,4,0,0,Math.PI*2);
  cx.fillStyle=`rgba(52,211,153,${0.9*pulse})`;cx.fill();

  // MOUTH
  cx.beginPath();cx.moveTo(bx-9,gy+4);cx.quadraticCurveTo(bx,gy+10,bx+9,gy+4);
  cx.strokeStyle=`rgba(52,211,153,0.7)`;cx.lineWidth=1.6;cx.stroke();

  // ANTENNA
  cx.beginPath();cx.moveTo(bx,gy-50);cx.lineTo(bx+14,gy-70);
  cx.strokeStyle=`rgba(52,211,153,0.55)`;cx.lineWidth=1.5;cx.stroke();
  cx.beginPath();cx.arc(bx+14,gy-70,4*pulse,0,Math.PI*2);
  cx.fillStyle=`rgba(52,211,153,${pulse})`;cx.fill();

  // ZZZ
  const zOff=(t*18)%38;
  ['z','z','Z'].forEach((z,i)=>{
    const zx=bx+33+i*11,zy=gy-48-i*13-zOff;
    if(zy>gy-106){
      cx.font=`bold ${9+i*3}px sans-serif`;
      cx.fillStyle=`rgba(167,139,250,${0.62-i*0.08})`;cx.fillText(z,zx,zy);
    }
  });
}

function drawTitle(bx){
  cx.font='bold 44px -apple-system,BlinkMacSystemFont,sans-serif';
  const g=cx.createLinearGradient(bx+88,0,bx+440,0);
  g.addColorStop(0,'#34d399');g.addColorStop(0.45,'#38bdf8');g.addColorStop(1,'#a78bfa');
  cx.fillStyle=g;cx.fillText('Artemis Hub',bx+90,H/2-6);
}

function loop(){
  t+=0.022;
  cx.fillStyle='#020617';cx.fillRect(0,0,W,H);
  drawStars();
  const bx=W/2-120,by=H/2+8;
  drawParticles(bx,by);
  drawBear(bx,by);
  drawTitle(bx);
  requestAnimationFrame(loop);
}
loop();
</script>
""", height=240)

# ── APP DATA ──────────────────────────────────────────────────
APPS = [
    # ── column 1 ──
    {"name":"Sol Energy Forecast",    "emoji":"⚡", "desc":"LSTM solar energy predictions in real time.",              "url":"https://solenergyforecast.streamlit.app/",         "img":"img_solar.png"},
    {"name":"Flower Classifier",      "emoji":"🌸", "desc":"Classify flower species with your trained model.",        "url":"https://tlflores.streamlit.app/",                  "img":"img_flowers.jpg"},
    {"name":"Translator",             "emoji":"🌐", "desc":"Smart AI translation across multiple languages.",         "url":"https://traductore.streamlit.app/",                "img":"img_translator.jpg"},
    {"name":"Image Analysis",         "emoji":"🏞️", "desc":"Understand and describe any image with AI vision.",      "url":"https://visionn.streamlit.app/",                   "img":"img_vision.jpg"},
    {"name":"Wordcloud",              "emoji":"☁️", "desc":"Visualize most frequent words in any text.",             "url":"https://wordcloud-1.streamlit.app/",               "img":"img_wordcloud.jpg"},
    # ── column 2 ──
    {"name":"LSTM Text Generator",    "emoji":"📝", "desc":"Generate coherent text with an LSTM network.",           "url":"https://textgeneratoor.streamlit.app/",            "img":"img_textgen.jpg"},
    {"name":"YOGI",                   "emoji":"🐶", "desc":"Image recognition using your Teachable Machine model.",  "url":"https://teachablem-yogi.streamlit.app/",           "img":"img_yogi.jpg"},
    {"name":"Sentiment Analysis",     "emoji":"❤️", "desc":"Detect positive, negative or neutral tone in text.",     "url":"https://sentimientos-1.streamlit.app/",            "img":"img_sentiment.png"},
    {"name":"Basic Neural Network",   "emoji":"🧠", "desc":"RNN app for time series sequence prediction.",           "url":"https://rnnbasica.streamlit.app/",                 "img":"img_rnn.jpg"},
    {"name":"OCR to Audio",           "emoji":"🔡", "desc":"Extract text from images via OCR and convert to audio.", "url":"https://ocr-audioo.streamlit.app/",                "img":"img_ocr_audio.jpg"},
    # ── column 3 ──
    {"name":"Advanced OCR",           "emoji":"📑", "desc":"Optical character recognition on complex documents.",    "url":"https://opticalcr.streamlit.app/",                 "img":"img_ocr_doc.png"},
    {"name":"Handwritten Digits",     "emoji":"✍️", "desc":"Draw a digit — the neural network reads it instantly.",  "url":"https://hzwi7bwfepy6scpu7pradh.streamlit.app/",   "img":"img_digits.jpg"},
    {"name":"Text to Speech",         "emoji":"🔊", "desc":"Convert any text into natural AI-generated speech.",    "url":"https://text-to-voic.streamlit.app/",              "img":"img_tts.png"},
    {"name":"Object Detection",       "emoji":"🔍", "desc":"Detect and label objects in images with YOLOv5.",       "url":"https://yolov55.streamlit.app/",                   "img":"img_yolo.jpg"},
    {"name":"Data Analysis",          "emoji":"📊", "desc":"AI agents explore, clean and chart your data.",         "url":"https://dataagentt.streamlit.app/",                "img":"img_data.png"},
    # ── column 4 ──
    {"name":"Convolutions",           "emoji":"🎛️", "desc":"See how convolutional filters transform images live.",   "url":"https://convoluciones.streamlit.app/",             "img":"img_conv.jpg"},
    {"name":"Cyber-Physical GPT",     "emoji":"🤖", "desc":"Interact with the physical world via ChatGPT.",         "url":"https://chatgptexploring.streamlit.app/",          "img":"img_cybergpt.png"},
    {"name":"Cyber-Physical Claude",  "emoji":"🧬", "desc":"Cyber-physical interaction powered by Claude AI.",      "url":"https://chatbot-antropic.streamlit.app/",          "img":"img_cyberclaude.jpg"},
    {"name":"RAG with PDF",           "emoji":"📚", "desc":"Upload a PDF and ask questions — RAG powered.",         "url":"https://chatpdefe.streamlit.app/",                 "img":"img_rag.png"},
    {"name":"Interactive Autoencoder","emoji":"🎲", "desc":"Explore and generate digits with a VAE model.",         "url":"https://aevminists.streamlit.app/",                "img":"img_vae.png"},
]

# ── SECTION LABEL ─────────────────────────────────────────────
st.markdown("""
<div style='text-align:center;font-size:11px;font-weight:600;letter-spacing:0.2em;
  text-transform:uppercase;color:#34d399;opacity:0.65;margin:4px 0 14px;'>
  Applications
</div>
""", unsafe_allow_html=True)

# ── GRID 4 × 5 ────────────────────────────────────────────────
cols = st.columns(4, gap="small")

for i, app in enumerate(APPS):
    with cols[i % 4]:
        try:
            img = Image.open(app["img"])
            st.image(img, use_container_width=True)
        except FileNotFoundError:
            st.image(
                "https://placehold.co/300x130/0a1628/34d399?text=" + app["name"].replace(" ", "+"),
                use_container_width=True
            )
        st.subheader(f"{app['emoji']} {app['name']}")
        st.write(app["desc"])
        st.write(f"[Open app →]({app['url']})")
        st.markdown("---")
