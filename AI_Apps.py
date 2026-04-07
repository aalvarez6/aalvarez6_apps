import streamlit as st
from PIL import Image

st.set_page_config(page_title="Artemis AI Hub", page_icon="🧬", layout="wide")

# ============================================================================
#  APPLICATIONS LIST (edit here easily)
# ============================================================================
APPS = [
    {
        "name": "Sol Energy Forecast",
        "desc": "Real‑time solar energy prediction with LSTM.",
        "img": "Energy Forecast.webp",
        "url": "https://solenergyforecast.streamlit.app/",
        "emoji": "⚡"
    },
    {
        "name": "BloomVision",
        "desc": "Classify flowers and plants using your trained model  ",
        "img": "BloomVision.png",
        "url": "https://tlflores.streamlit.app/",
        "emoji": "🌸"
    },
    {
        "name": "Polyglot AI",
        "desc": "Smart AI translation across multiple languages.",
        "img": "PolyglotAI.png",
        "url": "https://traductore.streamlit.app/",
        "emoji": "🌐"
    },
    {
        "name": "VisionX",
        "desc": "Understand and describe any image with AI vision.",
        "img": "VisionX.png",
        "url": "https://visionn.streamlit.app/",
        "emoji": "🏞️"
    },
    {
        "name": "Wordcloud",
        "desc": "Visualize most frequent words in any text.",
        "img": "WordCloud.png",
        "url": "https://wordcloud-1.streamlit.app/",
        "emoji": "☁️"
    },
    {
        "name": "NeuroText",
        "desc": "Generate coherent text with a Long Short Term Memory network. ",
        "img": "NeuroText.png",
        "url": "https://textgeneratoor.streamlit.app/",
        "emoji": "📝"
    },
    {
        "name": "YOGI",
        "desc": "Image recognition using your Teachable Machine model.",
        "img": "YOGI.png",
        "url": "https://teachablem-yogi.streamlit.app/",
        "emoji": "🐶"
    },
    {
        "name": "Sentiment Analysis",
        "desc": "Detect positive, negative or neutral tone in text.",
        "img": "Sentiment Analysis.png",
        "url": "https://sentimientos-1.streamlit.app/",
        "emoji": "❤️"
    },
    {
        "name": "Basic Neural Network",
        "desc": "Time series sequence prediction with a basic RNN.",
        "img": "Basic Neuronal Network.png",
        "url": "https://rnnbasica.streamlit.app/",
        "emoji": "🧠"
    },
    {
        "name": "Voice OCR",
        "desc": "Extract text from images via OCR and convert to audio.",
        "img": "Voice OCR.png",
        "url": "https://ocr-audioo.streamlit.app/",
        "emoji": "🔡"
    },
    {
        "name": "Advanced OCR",
        "desc": "Optical character recognition on complex documents.",
        "img": "Advanced OCR.png",
        "url": "https://opticalcr.streamlit.app/",
        "emoji": "📑"
    },
    {
        "name": "Handwritten Digits",
        "desc": "Draw a digit — the neural network reads it instantly.",
        "img": "handwritten Digits.png",
        "url": "https://hzwi7bwfepy6scpu7pradh.streamlit.app/",
        "emoji": "✍️"
    },
    {
        "name": "Text to Speech",
        "desc": "Convert any text into natural AI‑generated speech.",
        "img": "Text to Speech.png",
        "url": "https://text-to-voic.streamlit.app/",
        "emoji": "🔊"
    },
    {
        "name": "Object Detection",
        "desc": "Detect and label objects in images with YOLOv5.",
        "img": "YOLOv5.png",
        "url": "https://yolov55.streamlit.app/",
        "emoji": "🔍"
    },
    {
        "name": "Data Analysis",
        "desc": "AI agents explore, clean and chart your data.",
        "img": "Cyber-Physical.png",
        "url": "https://dataagentt.streamlit.app/",
        "emoji": "📊"
    },
    {
        "name": "Convolutions",
        "desc": "See how convolutional filters transform images live.",
        "img": "Convolutions.png",
        "url": "https://convoluciones.streamlit.app/",
        "emoji": "🎛️"
    },
    {
        "name": "Cyber-Physical GPT",
        "desc": "Interact with the physical world via ChatGPT.",
        "img": "Cyber-Physical.png",
        "url": "https://chatgptexploring.streamlit.app/",
        "emoji": "🤖"
    },
    {
        "name": "Cyber-Physical Claude",
        "desc": "Cyber‑physical interaction powered by Claude AI.",
        "img": "Cyber-Physical.png",
        "url": "https://chatbot-antropic.streamlit.app/",
        "emoji": "🧬"
    },
    {
        "name": "RAG with PDF",
        "desc": "Upload a PDF and ask questions — RAG powered.",
        "img": "RAG with PDF.png",
        "url": "https://chatpdefe.streamlit.app/",
        "emoji": "📚"
    },
    {
        "name": "Interactive Autoencoder",
        "desc": "Explore and generate digits with a VAE model.",
        "img": "Autoencoder VAE.png",
        "url": "https://aevminists.streamlit.app/",
        "emoji": "🎲"
    }
]

# ============================================================================
#  macOS DARK STYLE (rounded cards, black background)
# ============================================================================
st.markdown("""
<style>
    html, body, [class*="css"] {
        font-family: -apple-system, BlinkMacSystemFont, "San Francisco", "Segoe UI", sans-serif;
    }
    .stApp {
        background-color: #000000;
    }
    [data-testid="stSidebar"] {
        background-color: #1c1c1e;
        border-right: 1px solid #2c2c2e;
    }
    [data-testid="stSidebar"] * {
        color: #f5f5f7;
    }
    .block-container {
        max-width: 1400px;
        padding-top: 0rem;
    }
    /* Individual card */
    .apple-card {
        background: #1c1c1e;
        border-radius: 20px;
        padding: 1rem;
        margin-bottom: 1.2rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.5);
        transition: all 0.2s ease;
        border: 1px solid #2c2c2e;
        text-align: center;
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    .apple-card:hover {
        transform: translateY(-3px);
        background: #2c2c2e;
        border-color: #3a3a3c;
    }
    .apple-card img {
        border-radius: 16px;
        width: 100%;
        aspect-ratio: 1 / 1;
        object-fit: cover;
        margin-bottom: 0.8rem;
        background: #2c2c2e;
    }
    .apple-card h4 {
        font-size: 1rem;
        font-weight: 600;
        margin: 0.5rem 0 0.2rem;
        color: #ffffff;
    }
    .apple-card p {
        font-size: 0.75rem;
        color: #a1a1a6;
        line-height: 1.3;
        margin-bottom: 0.8rem;
        flex-grow: 1;
    }
    .stLinkButton button {
        background: #007aff;
        color: white;
        border: none;
        border-radius: 980px;
        padding: 0.4rem 1rem;
        font-size: 0.75rem;
        font-weight: 500;
        width: 100%;
    }
    .stLinkButton button:hover {
        background: #005fcb;
    }
    .footer {
        text-align: center;
        color: #636366;
        padding: 1rem;
        font-size: 0.7rem;
        border-top: 1px solid #2c2c2e;
        margin-top: 2rem;
    }
    hr {
        border-color: #2c2c2e;
    }
    [data-testid="column"] {
        padding-left: 8px !important;
        padding-right: 8px !important;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
#  ANIMATED LOGO (ARTEMIS BEAR + PARTICLES)
# ============================================================================
st.components.v1.html("""
<div style="background:#000000; border-radius:20px; padding:0px 0 0; margin-bottom:0px;">
  <canvas id="artemisCanvas" width="1000" height="220"
    style="display:block; margin:0 auto; cursor:crosshair; width:100%; height:auto; max-width:1000px;"></canvas>
  <div style="text-align:center; font-family:-apple-system,BlinkMacSystemFont,sans-serif;
    font-size:11px; font-weight:600; letter-spacing:0.22em; text-transform:uppercase;
    color:#34d399; opacity:0.7; padding:4px 0 12px;">AI Applications Platform</div>
</div>
<script>
(function(){
const canvas = document.getElementById('artemisCanvas');
const ctx = canvas.getContext('2d');
let W = canvas.width, H = canvas.height;
function resizeCanvas() {
    const container = canvas.parentElement;
    const maxW = Math.min(1000, container.clientWidth);
    canvas.style.width = maxW + 'px';
    canvas.style.height = 'auto';
    canvas.width = maxW;
    canvas.height = 220 * (maxW / 1000);
    W = canvas.width;
    H = canvas.height;
}
resizeCanvas();
window.addEventListener('resize', resizeCanvas);

let mouse = { x: W/2, y: H/2 };
canvas.addEventListener('mousemove', e => {
    const rect = canvas.getBoundingClientRect();
    const scaleX = canvas.width / rect.width;
    const scaleY = canvas.height / rect.height;
    mouse.x = (e.clientX - rect.left) * scaleX;
    mouse.y = (e.clientY - rect.top) * scaleY;
});
let t = 0;

const STARS = Array.from({length:80}, () => ({
    x: Math.random() * W, y: Math.random() * H,
    r: Math.random() * 1.2 + 0.2, a: Math.random() * 0.7 + 0.2,
    va: (Math.random() - 0.5) * 0.008
}));
const PART = Array.from({length:35}, () => ({
    x: Math.random() * W, y: Math.random() * H,
    vx: (Math.random() - 0.5) * 0.5, vy: (Math.random() - 0.5) * 0.5,
    r: Math.random() * 2 + 0.5,
    c: ['52,211,153','167,139,250','56,189,248'][Math.floor(Math.random()*3)],
    a: Math.random() * 0.5 + 0.25
}));

function drawStars() {
    STARS.forEach(s => {
        s.a += s.va;
        if (s.a > 0.9 || s.a < 0.1) s.va *= -1;
        ctx.beginPath();
        ctx.arc(s.x, s.y, s.r, 0, Math.PI*2);
        ctx.fillStyle = `rgba(255,255,255,${s.a})`;
        ctx.fill();
    });
}

function drawParticles(bx, by) {
    PART.forEach(p => {
        p.x += p.vx;
        p.y += p.vy;
        if (p.x < 0) p.x = W;
        if (p.x > W) p.x = 0;
        if (p.y < 0) p.y = H;
        if (p.y > H) p.y = 0;
        const dx = bx - p.x, dy = by - p.y, d = Math.hypot(dx, dy);
        if (d < 140 && d > 30) {
            p.vx += dx / d * 0.012;
            p.vy += dy / d * 0.012;
        }
        const sp = Math.hypot(p.vx, p.vy);
        if (sp > 1.1) { p.vx *= 0.93; p.vy *= 0.93; }
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI*2);
        ctx.fillStyle = `rgba(${p.c},${p.a})`;
        ctx.fill();
    });
    for (let i = 0; i < PART.length; i++) {
        for (let j = i+1; j < PART.length; j++) {
            const dx = PART[i].x - PART[j].x, dy = PART[i].y - PART[j].y;
            const d = Math.hypot(dx, dy);
            if (d < 50) {
                ctx.beginPath();
                ctx.moveTo(PART[i].x, PART[i].y);
                ctx.lineTo(PART[j].x, PART[j].y);
                ctx.strokeStyle = `rgba(52,211,153,${0.12 * (1 - d/50)})`;
                ctx.lineWidth = 0.5;
                ctx.stroke();
            }
        }
    }
}

function drawBear(bx, by) {
    const bob = Math.sin(t*1.6) * 3;
    const gy = by + bob;
    const pulse = 0.7 + 0.3 * Math.sin(t*2.5);
    const pulse2 = 0.6 + 0.4 * Math.sin(t*2.5+1);

    // Aura
    const aura = ctx.createRadialGradient(bx, gy, 5, bx, gy, 90);
    aura.addColorStop(0, 'rgba(52,211,153,0.16)');
    aura.addColorStop(0.5, 'rgba(56,189,248,0.06)');
    aura.addColorStop(1, 'rgba(52,211,153,0)');
    ctx.beginPath();
    ctx.arc(bx, gy, 90, 0, Math.PI*2);
    ctx.fillStyle = aura;
    ctx.fill();

    // Left claw
    ctx.save();
    ctx.translate(bx-52, gy+22);
    ctx.rotate(-0.38 + Math.sin(t*1.6)*0.05);
    for (let c=0; c<3; c++) {
        const ang = -0.5 + c*0.5, len = 20 + c*3;
        ctx.beginPath();
        ctx.moveTo(0,0);
        ctx.quadraticCurveTo(Math.cos(ang-0.3)*len*0.6, Math.sin(ang-0.3)*len*0.6-6, Math.cos(ang)*len, Math.sin(ang)*len-8);
        ctx.strokeStyle = `rgba(52,211,153,${0.88*pulse})`;
        ctx.lineWidth = 3.2;
        ctx.lineCap = 'round';
        ctx.stroke();
        ctx.beginPath();
        ctx.arc(Math.cos(ang)*len, Math.sin(ang)*len-8, 2.8, 0, Math.PI*2);
        ctx.fillStyle = `rgba(52,211,153,${pulse})`;
        ctx.fill();
    }
    ctx.beginPath();
    ctx.ellipse(0, 6, 9, 14, 0, 0, Math.PI*2);
    const aG = ctx.createRadialGradient(0,0,2,0,6,14);
    aG.addColorStop(0, 'rgba(56,189,248,0.95)');
    aG.addColorStop(1, 'rgba(13,80,60,0.75)');
    ctx.fillStyle = aG;
    ctx.fill();
    ctx.strokeStyle = `rgba(52,211,153,${0.65*pulse})`;
    ctx.lineWidth = 1;
    ctx.stroke();
    ctx.restore();

    // Right claw
    ctx.save();
    ctx.translate(bx+52, gy+22);
    ctx.rotate(0.38 + Math.sin(t*1.6+1)*0.05);
    for (let c=0; c<3; c++) {
        const ang = Math.PI + 0.5 - c*0.5, len = 20 + c*3;
        ctx.beginPath();
        ctx.moveTo(0,0);
        ctx.quadraticCurveTo(Math.cos(ang+0.3)*len*0.6, Math.sin(ang+0.3)*len*0.6-6, Math.cos(ang)*len, Math.sin(ang)*len-8);
        ctx.strokeStyle = `rgba(52,211,153,${0.88*pulse})`;
        ctx.lineWidth = 3.2;
        ctx.stroke();
        ctx.beginPath();
        ctx.arc(Math.cos(ang)*len, Math.sin(ang)*len-8, 2.8, 0, Math.PI*2);
        ctx.fillStyle = `rgba(52,211,153,${pulse})`;
        ctx.fill();
    }
    ctx.beginPath();
    ctx.ellipse(0, 6, 9, 14, 0, 0, Math.PI*2);
    const aG2 = ctx.createRadialGradient(0,0,2,0,6,14);
    aG2.addColorStop(0, 'rgba(56,189,248,0.95)');
    aG2.addColorStop(1, 'rgba(13,80,60,0.75)');
    ctx.fillStyle = aG2;
    ctx.fill();
    ctx.strokeStyle = `rgba(52,211,153,${0.65*pulse})`;
    ctx.stroke();
    ctx.restore();

    // Body
    ctx.beginPath();
    ctx.ellipse(bx, gy+36, 28, 26, 0, 0, Math.PI*2);
    const bG = ctx.createRadialGradient(bx-6, gy+26, 4, bx, gy+36, 30);
    bG.addColorStop(0, 'rgba(56,189,248,0.95)');
    bG.addColorStop(0.5, 'rgba(14,116,144,0.85)');
    bG.addColorStop(1, 'rgba(6,50,70,0.9)');
    ctx.fillStyle = bG;
    ctx.fill();
    ctx.strokeStyle = `rgba(52,211,153,${0.8*pulse})`;
    ctx.lineWidth = 1.3;
    ctx.stroke();
    for (let i=0; i<4; i++) {
        ctx.beginPath();
        ctx.arc(bx-5 + i*2.5, gy+32 + i*3.5, 1, 0, Math.PI*2);
        ctx.fillStyle = `rgba(52,211,153,${0.4+0.3*Math.sin(t*3+i)})`;
        ctx.fill();
    }

    // Ears
    [bx-25, bx+25].forEach(ex => {
        ctx.beginPath();
        ctx.arc(ex, gy-40, 13, 0, Math.PI*2);
        const eG = ctx.createRadialGradient(ex, gy-40, 2, ex, gy-40, 13);
        eG.addColorStop(0, 'rgba(56,189,248,0.92)');
        eG.addColorStop(1, 'rgba(6,50,70,0.82)');
        ctx.fillStyle = eG;
        ctx.fill();
        ctx.strokeStyle = `rgba(52,211,153,${0.7*pulse})`;
        ctx.lineWidth = 1;
        ctx.stroke();
        ctx.beginPath();
        ctx.arc(ex, gy-40, 6, 0, Math.PI*2);
        ctx.fillStyle = `rgba(52,211,153,${0.55*pulse2})`;
        ctx.fill();
    });

    // Head
    ctx.beginPath();
    ctx.ellipse(bx, gy-12, 35, 33, 0, 0, Math.PI*2);
    const hG = ctx.createRadialGradient(bx-8, gy-20, 4, bx, gy-12, 35);
    hG.addColorStop(0, 'rgba(56,189,248,0.95)');
    hG.addColorStop(0.6, 'rgba(14,116,144,0.88)');
    hG.addColorStop(1, 'rgba(6,50,70,0.92)');
    ctx.fillStyle = hG;
    ctx.fill();
    ctx.strokeStyle = `rgba(52,211,153,${0.75*pulse})`;
    ctx.lineWidth = 1.3;
    ctx.stroke();

    ctx.beginPath();
    ctx.ellipse(bx, gy+2, 18, 15, 0, 0, Math.PI*2);
    ctx.fillStyle = 'rgba(56,189,248,0.22)';
    ctx.fill();

    // Eyes (follow mouse)
    const oX = Math.max(-5, Math.min(5, (mouse.x - bx) * 0.07));
    const oY = Math.max(-3, Math.min(3, (mouse.y - gy) * 0.05));
    [bx-13, bx+13].forEach(ex => {
        ctx.beginPath();
        ctx.ellipse(ex, gy-18, 8, 9, 0, 0, Math.PI*2);
        ctx.fillStyle = 'rgba(220,255,245,0.93)';
        ctx.fill();
        ctx.strokeStyle = `rgba(52,211,153,${0.8*pulse})`;
        ctx.lineWidth = 0.8;
        ctx.stroke();
        ctx.beginPath();
        ctx.arc(ex+oX, gy-18+oY, 4, 0, Math.PI*2);
        ctx.fillStyle = '#050e14';
        ctx.fill();
        ctx.beginPath();
        ctx.arc(ex+oX, gy-18+oY, 1.8, 0, Math.PI*2);
        ctx.fillStyle = `rgba(52,211,153,${0.9*pulse})`;
        ctx.fill();
        ctx.beginPath();
        ctx.arc(ex+oX+1.5, gy-20+oY, 1, 0, Math.PI*2);
        ctx.fillStyle = 'rgba(255,255,255,0.8)';
        ctx.fill();
    });

    // Nose
    ctx.beginPath();
    ctx.ellipse(bx, gy-4, 5.5, 3.8, 0, 0, Math.PI*2);
    ctx.fillStyle = `rgba(52,211,153,${0.9*pulse})`;
    ctx.fill();

    // Mouth
    ctx.beginPath();
    ctx.moveTo(bx-8, gy+4);
    ctx.quadraticCurveTo(bx, gy+10, bx+8, gy+4);
    ctx.strokeStyle = `rgba(52,211,153,0.7)`;
    ctx.lineWidth = 1.5;
    ctx.stroke();

    // Antenna
    ctx.beginPath();
    ctx.moveTo(bx, gy-46);
    ctx.lineTo(bx+12, gy-64);
    ctx.strokeStyle = `rgba(52,211,153,0.55)`;
    ctx.lineWidth = 1.3;
    ctx.stroke();
    ctx.beginPath();
    ctx.arc(bx+12, gy-64, 3.5*pulse, 0, Math.PI*2);
    ctx.fillStyle = `rgba(52,211,153,${pulse})`;
    ctx.fill();

    // ZZZ
    const zOff = (t*16) % 34;
    ['z','z','Z'].forEach((z,i)=>{
        const zx = bx+30 + i*9, zy = gy-44 - i*12 - zOff;
        if (zy > gy-98) {
            ctx.font = `bold ${8+i*2}px sans-serif`;
            ctx.fillStyle = `rgba(167,139,250,${0.6 - i*0.08})`;
            ctx.fillText(z, zx, zy);
        }
    });
}

function drawTitle(bx) {
    ctx.font = 'bold 40px -apple-system,BlinkMacSystemFont,sans-serif';
    const grad = ctx.createLinearGradient(bx+80, 0, bx+360, 0);
    grad.addColorStop(0, '#34d399');
    grad.addColorStop(0.5, '#38bdf8');
    grad.addColorStop(1, '#a78bfa');
    ctx.fillStyle = grad;
    ctx.fillText('Artemis Hub', bx+85, H/2 - 6);
}

function animate() {
    t += 0.022;
    ctx.fillStyle = '#000000';
    ctx.fillRect(0, 0, W, H);
    drawStars();
    const bx = W/2 - 110, by = H/2 + 8;
    drawParticles(bx, by);
    drawBear(bx, by);
    drawTitle(bx);
    requestAnimationFrame(animate);
}
animate();
})();
</script>
""", height=250)

# ============================================================================
#  SIDEBAR
# ============================================================================
with st.sidebar:
    st.markdown("### 🧠 Artificial Intelligence")
    st.write(
        "AI improves decision‑making with data, automates routine tasks, "
        "and provides advanced real‑time analysis — greater efficiency "
        "across every field."
    )
    st.markdown("---")
    st.markdown("### 🔗 External Resources")
    st.markdown("[Pages & Exercises](https://sites.google.com/view/aplicacionesdeia/inicio)")
    st.markdown("---")
    st.caption("Artemis Hub · v3.0")

# ============================================================================
#  APPLICATIONS GRID (4 columns)
# ============================================================================
st.markdown("""
<div style="text-align:center; font-size:12px; font-weight:600; letter-spacing:0.2em;
  text-transform:uppercase; color:#34d399; opacity:0.7; margin: 10px 0 20px;">
  ⚡ AVAILABLE APPLICATIONS ⚡
</div>
""", unsafe_allow_html=True)

cols = st.columns(4, gap="medium")
for idx, app in enumerate(APPS):
    with cols[idx % 4]:
        try:
            img = Image.open(app["img"])
            st.image(img, use_container_width=True)
        except:
            st.markdown(f"""
            <div style="background:#1c1c1e; border-radius:16px; aspect-ratio:1/1;
                        display:flex; align-items:center; justify-content:center;
                        margin-bottom:0.8rem; font-size:3rem;">
                {app['emoji']}
            </div>
            """, unsafe_allow_html=True)
        st.markdown(f"<h4 style='text-align:center;'>{app['emoji']} {app['name']}</h4>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align:center;'>{app['desc']}</p>", unsafe_allow_html=True)
        st.link_button("Open App", app["url"], use_container_width=True)

# ============================================================================
#  FOOTER
# ============================================================================
st.markdown('<div class="footer">🍎 Artemis Hub Design • Uniform cards • All apps working</div>', unsafe_allow_html=True)
