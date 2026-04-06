import streamlit as st
from PIL import Image

st.markdown("""
<style>
  /* More space between columns */
  [data-testid="column"] {
    padding-left: 12px !important;
    padding-right: 12px !important;
  }
  /* More vertical space between items inside each column */
  [data-testid="column"] .stImage,
  [data-testid="column"] h3,
  [data-testid="column"] p {
    margin-bottom: 10px !important;
  }
  /* Divider between apps inside a column */
  [data-testid="column"] hr {
    margin: 20px 0 !important;
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

col1, col2, col3, col4 = st.columns(4, gap="large")

with col1:

  # 1
  st.markdown("---")
  st.subheader("⚡ Sol Energy Forecast")
  image = Image.open('Energy_forecast.png')
  st.image(image, width=100)
  st.write("In the following link we will use one of the Artificial Intelligence applications. LSTM for energy predictions.")
  url = "https://solenergyforecast.streamlit.app/"
  st.write(f"Sol Energy Forecast: [Link]({url})")

  # 2
  st.markdown("---")
  st.subheader("🌸 Flower Classifier")
  image = Image.open('photo_9_2026-03-17_16-25-34.jpg')
  st.image(image, width=100)
  st.write("In the following link we will see how you can use your trained model to classify flowers.")
  url = "https://tlflores.streamlit.app/"
  st.write(f"🌸 Flower Classifier: [Link]({url})")

  # 3
  st.markdown("---")
  st.subheader("🌐 Translator")
  image = Image.open('OIG5.jpg')
  st.image(image, width=100)
  st.write("In the following link we will see an AI application for translation.")
  url = "https://traductore.streamlit.app/"
  st.write(f"Translator: [Link]({url})")

  # 4
  st.markdown("---")
  st.subheader("🏞️ Image Analysis")
  image = Image.open('OIG5.jpg')
  st.image(image, width=100)
  st.write("In the following link we will see an AI application for image analysis.")
  url = "https://visionn.streamlit.app/"
  st.write(f"Vision: [Link]({url})")

  # 5
  st.markdown("---")
  st.subheader("☁️ Wordcloud")
  image = Image.open('OIG5.jpg')
  st.image(image, width=100)
  st.write("In the following link we will see an AI application to visualize the word cloud of generative AI.")
  url = "https://wordcloud-1.streamlit.app/"
  st.write(f"Wordcloud: [Link]({url})")


with col2:

  # 1
  st.markdown("---")
  st.subheader("📝 Text Generator")
  image = Image.open('OIG5.jpg')
  st.image(image, width=100)
  st.write("In the following link we will see how you can use the LSTM Text Generator.")
  url = "https://textgeneratoor.streamlit.app/"
  st.write(f"LSTM Text Generator: [Link]({url})")

  # 2
  st.markdown("---")
  st.subheader("🧘‍♀️  YOGI")
  image = Image.open('OIG5.jpg')
  st.image(image, width=100)
  st.write("In the following link we will see how to use your trained model for image recognition.")
  url = "https://teachablem-yogi.streamlit.app/"
  st.write(f"YOGI: [Link]({url})")

  # 3
  st.markdown("---")
  st.subheader("❤️ Sentiment Analysis")
  image = Image.open('txt_to_audio.png')
  st.image(image, width=100)
  st.write("In the following link we will see sentiment analysis based on expressions.")
  url = "https://sentimientos-1.streamlit.app/"
  st.write(f"Sentiment Analysis: [Link]({url})")

  # 4
  st.markdown("---")
  st.subheader("🧠 Basic Neural Network")
  image = Image.open('OIG8.jpg')
  st.image(image, width=100)
  st.write("In the following we will see an application that uses RNN for time series prediction.")
  url = "https://rnnbasica.streamlit.app/"
  st.write(f"Basic Neural Network: [Link]({url})")

  # 5
  st.markdown("---")
  st.subheader("🔡 Optical Character Recognition")
  image = Image.open('OIG3.jpg')
  st.image(image, width=100)
  st.write("In the following link we will see how Optical Character Recognition (OCR) is used with audio.")
  url = "https://ocr-audioo.streamlit.app/"
  st.write(f"OCR: [Link]({url})")


with col3:

  # 1
  st.markdown("---")
  st.subheader("📑 Advanced OCR")
  image = Image.open('Chat_pdf.png')
  st.image(image, width=100)
  st.write("In the following we will see an application that uses Optical Character Recognition (OCR).")
  url = "https://opticalcr.streamlit.app/"
  st.write(f"Vision: [Link]({url})")

  # 2
  st.markdown("---")
  st.subheader("✍️ Handwritten Digit Detector")
  image = Image.open('OIG4.jpg')
  st.image(image, width=100)
  st.write("In the following link we will see the capability of ✍️ Handwritten Digit Detection.")
  url = "https://hzwi7bwfepy6scpu7pradh.streamlit.app/"
  st.write(f"Vision: [Link]({url})")

  # 3
  st.markdown("---")
  st.subheader("🔊 Text to Speech")
  image = Image.open('txt_to_audio2.png')
  st.image(image, width=100)
  st.write("In the following link we will use one of the Artificial Intelligence applications for text-to-speech conversion.")
  url = "https://text-to-voic.streamlit.app/"
  st.write(f"Text to Speech: [Link]({url})")

  # 4
  st.markdown("---")
  st.subheader("🔍 Object Detection in Images")
  image = Image.open('OIG4.jpg')
  st.image(image, width=100)
  st.write("In the following link we will see 🔍 Object Detection in Images.")
  url = "https://yolov55.streamlit.app/"
  st.write(f"YOLO: [Link]({url})")

  # 5
  st.markdown("---")
  st.subheader("📊 Data Analysis")
  image = Image.open('data_analisis.png')
  st.image(image, width=100)
  st.write("In the following link we will see how data can be analyzed using AI agents.")
  url = "https://dataagentt.streamlit.app/"
  st.write(f"Data: [Link]({url})")


with col4:

  # 1
  st.markdown("---")
  st.subheader("🎛️ Convolutions")
  image = Image.open('OIG6.jpg')
  st.image(image, width=100)
  st.write("In the following link explore how convolutional filters transform images.")
  url = "https://convoluciones.streamlit.app/"
  st.write(f"Convolutions: [Link]({url})")

  # 2
  st.markdown("---")
  st.subheader("🤖 Cyber-Physical System (ChatGPT)")
  image = Image.open('Chat_pdf.png')
  st.image(image, width=100)
  st.write("In the following link we will see the capacity for interaction with the physical world (ChatGPT).")
  url = "https://chatgptexploring.streamlit.app/"
  st.write(f"RAG: [Link]({url})")

  # 3
  st.markdown("---")
  st.subheader("🧬 Cyber-Physical System (Anthropic)")
  image = Image.open('OIG6.jpg')
  st.image(image, width=100)
  st.write("In the following link we will see the capacity for interaction with the physical world (ChatAnthropic).")
  url = "https://chatbot-antropic.streamlit.app/"
  st.write(f"Vision: [Link]({url})")

  # 4
  st.markdown("---")
  st.subheader("📚 Retrieval-Augmented Generation (RAG)")
  image = Image.open('Chat_pdf.png')
  st.image(image, width=100)
  st.write("In the following we will see an application that uses RAG from a document (PDF).")
  url = "https://chatpdefe.streamlit.app/"
  st.write(f"RAG: [Link]({url})")

  # 5
  st.markdown("---")
  st.subheader("🎲 Interactive Autoencoder")
  image = Image.open('Chat_pdf.png')
  st.image(image, width=100)
  st.write("In the following we will see an interactive Variational Autoencoder application to explore and generate digits.")
  url = "https://aevminists.streamlit.app/"
  st.write(f"RAG: [Link]({url})")
