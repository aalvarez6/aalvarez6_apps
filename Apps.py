import streamlit as st
from PIL import Image

st.markdown("""
<style>
  [data-testid="column"] {
    padding-left: 6px !important;
    padding-right: 6px !important;
  }
  [data-testid="column"] .stImage {
    margin-bottom: 4px !important;
  }
  [data-testid="column"] h3 {
    margin-bottom: 4px !important;
    margin-top: 16px !important;
    font-size: 0.95rem !important;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  [data-testid="column"] p {
    margin-bottom: 4px !important;
    font-size: 0.82rem !important;
  }
</style>
""", unsafe_allow_html=True)

st.title("Artificial Intelligence Applications.")

with st.sidebar:
  st.subheader("Artificial Intelligence.")
  parrafo = (
    "Artificial intelligence improves decision-making using data, "
    "automates routine tasks, and provides advanced real-time analysis, "
    "resulting in greater efficiency and precision across various fields."
  )
  st.write(parrafo)

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.write(f"Link to pages and exercises: [Link]({url_ia})")

col1, col2, col3, col4 = st.columns(4, gap="small")

with col1:

  st.subheader("⚡ Sol Energy Forecast  ")
  image = Image.open('Energy_forecast.png')
  st.image(image, width=200)
  st.write("LSTM predictions for solar energy generation in real time.")
  url = "https://solenergyforecast.streamlit.app/"
  st.write(f"Sol Energy Forecast: [Link]({url})")

  st.subheader("🌸 Flower Classifier     ")
  image = Image.open('photo_9_2026-03-17_16-25-34.jpg')
  st.image(image, width=200)
  st.write("Classify flower species using your own trained model.")
  url = "https://tlflores.streamlit.app/"
  st.write(f"Flower Classifier: [Link]({url})")

  st.subheader("🌐 Translator            ")
  image = Image.open('OIG5.jpg')
  st.image(image, width=200)
  st.write("AI-powered translation app supporting multiple languages.")
  url = "https://traductore.streamlit.app/"
  st.write(f"Translator: [Link]({url})")

  st.subheader("🏞️ Image Analysis        ")
  image = Image.open('OIG5.jpg')
  st.image(image, width=200)
  st.write("Analyze and describe the content of any image with AI.")
  url = "https://visionn.streamlit.app/"
  st.write(f"Image Analysis: [Link]({url})")

  st.subheader("☁️ Wordcloud             ")
  image = Image.open('OIG5.jpg')
  st.image(image, width=200)
  st.write("Visualize the most frequent words in any text with AI.")
  url = "https://wordcloud-1.streamlit.app/"
  st.write(f"Wordcloud: [Link]({url})")


with col2:

  st.subheader("📝 Text Generator   ")
  image = Image.open('OIG5.jpg')
  st.image(image, width=200)
  st.write("Generate coherent text using an LSTM neural network model.")
  url = "https://textgeneratoor.streamlit.app/"
  st.write(f"LSTM Text Generator: [Link]({url})")

  st.subheader("🐶 YOGI    ")
  image = Image.open('OIG5.jpg')
  st.image(image, width=200)
  st.write("Use your Teachable Machine model for image recognition.")
  url = "https://teachablem-yogi.streamlit.app/"
  st.write(f"YOGI: [Link]({url})")

  st.subheader("❤️ Sentiment Analysis    ")
  image = Image.open('txt_to_audio.png')
  st.image(image, width=200)
  st.write("Detect positive, negative or neutral tone in any text.")
  url = "https://sentimientos-1.streamlit.app/"
  st.write(f"Sentiment Analysis: [Link]({url})")

  st.subheader("🧠 Neural Network  ")
  image = Image.open('OIG8.jpg')
  st.image(image, width=200)
  st.write("RNN application for time series sequence prediction.")
  url = "https://rnnbasica.streamlit.app/"
  st.write(f"Basic Neural Network: [Link]({url})")

  st.subheader("🔡 OCR to Audio          ")
  image = Image.open('OIG3.jpg')
  st.image(image, width=200)
  st.write("Extract text from images using OCR and convert to audio.")
  url = "https://ocr-audioo.streamlit.app/"
  st.write(f"OCR to Audio: [Link]({url})")


with col3:

  st.subheader("📑 Advanced OCR          ")
  image = Image.open('Chat_pdf.png')
  st.image(image, width=200)
  st.write("Advanced optical character recognition on complex documents.")
  url = "https://opticalcr.streamlit.app/"
  st.write(f"Advanced OCR: [Link]({url})")

  st.subheader("Handwritten Digits ✍️")
  image = Image.open('OIG4.jpg')
  st.image(image, width=200)
  st.write("Draw a digit and the neural network recognizes it instantly.")
  url = "https://hzwi7bwfepy6scpu7pradh.streamlit.app/"
  st.write(f"Handwritten Digits: [Link]({url})")

  st.subheader("🔊 Text to Speech        ")
  image = Image.open('txt_to_audio2.png')
  st.image(image, width=200)
  st.write("Convert any text into natural speech audio with AI.")
  url = "https://text-to-voic.streamlit.app/"
  st.write(f"Text to Speech: [Link]({url})")

  st.subheader("🔍 Object Detection      ")
  image = Image.open('OIG4.jpg')
  st.image(image, width=200)
  st.write("Detect and label objects in images using YOLOv5 in real time.")
  url = "https://yolov55.streamlit.app/"
  st.write(f"Object Detection: [Link]({url})")

  st.subheader("📊 Data Analysis         ")
  image = Image.open('data_analisis.png')
  st.image(image, width=200)
  st.write("AI agents explore, clean and visualize your data automatically.")
  url = "https://dataagentt.streamlit.app/"
  st.write(f"Data Analysis: [Link]({url})")


with col4:

  st.subheader("🎛️ Convolutions")
  image = Image.open('OIG6.jpg')
  st.image(image, width=200)
  st.write("Explore how convolutional filters transform images live.")
  url = "https://convoluciones.streamlit.app/"
  st.write(f"Convolutions: [Link]({url})")

  st.subheader("🤖 Cyber-Physical")
  image = Image.open('Chat_pdf.png')
  st.image(image, width=200)
  st.write("Interact with the physical world using ChatGPT as the AI engine.")
  url = "https://chatgptexploring.streamlit.app/"
  st.write(f"Cyber-Physical GPT: [Link]({url})")

  st.subheader("🧬 Cyber-Physical")
  image = Image.open('OIG6.jpg')
  st.image(image, width=200)
  st.write("Cyber-physical interaction powered by Anthropic's Claude model.")
  url = "https://chatbot-antropic.streamlit.app/"
  st.write(f"Cyber-Physical Claude: [Link]({url})")

  st.subheader("📚 RAG with PDF          ")
  image = Image.open('Chat_pdf.png')
  st.image(image, width=200)
  st.write("Upload a PDF and ask questions using Retrieval-Augmented Generation.")
  url = "https://chatpdefe.streamlit.app/"
  st.write(f"RAG with PDF: [Link]({url})")

  st.subheader("🎲 Interactive Autoencoder")
  image = Image.open('Chat_pdf.png')
  st.image(image, width=200)
  st.write("Explore and generate digits with an interactive Variational Autoencoder.")
  url = "https://aevminists.streamlit.app/"
  st.write(f"Autoencoder: [Link]({url})")
