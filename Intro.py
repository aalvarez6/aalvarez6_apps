import streamlit as st
from PIL import Image
st.title("Aplicaciones de Inteligencia Artificial.")


with st.sidebar:
  st.subheader("Inteligencia Artificial.")
  parrafo = (
    "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
    "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
    "resulta en una mayor eficiencia y precisión en diversos campos."
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"

st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")
col1, col2, col3, col4 = st.columns(4)

with col1:

 st.subheader("Sol Energy Forecast")
 image = Image.open('Energy_forecast.png')
 st.image(image, width=200)
 st.write("En el siguiente enlace usaremos una de las aplicaciones de Inteligencia Artificial. LSTM para predicciones de energía") 
 url = "https://solenergyforecast.streamlit.app/"
 st.write(f"Sol Energy Forecast: [Enlace]({url})")
 
 #2
 st.subheader("🌸 Clasificador de Flores")
 image = Image.open('photo_9_2026-03-17_16-25-34.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos cómo puedes usar tu modelo entrenado para clasificar flores") 
 url = "https://tlflores.streamlit.app/"
 st.write(f"🌸 Clasificador de Flores: [Enlace]({url})")

 #3
 st.subheader("Traductor")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos una aplicación de IA para traducción")
 url = "https://traductore.streamlit.app/"
 st.write(f"Traductor: [Enlace]({url})")

 #4
 st.subheader("Análisis de Imagen 🏞️")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos una aplicación de IA para traducción")
 url = "https://visionn.streamlit.app/"
 st.write(f"Visión: [Enlace]({url})")

#5
 st.subheader("Wordcloud")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos una aplicación de IA para ver la nube de palabras del funcionamiento de IA gen")
 url = "https://wordcloud-1.streamlit.app/"
 st.write(f"Wordcloud: [Enlace]({url})")


with col2:
  
 #1
 st.subheader("Generador de Texto LSTM")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos cómo puedes usar Generador de Texto LSTM.") 
 url = "https://textgeneratoor.streamlit.app/"
 st.write(f"Generador de Texto LSTM: [Enlace]({url})")

 #2
 st.subheader("YOGI")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos cómo usar tu modelo entrenado para el reconocimiento de imagenes.") 
 url = "https://teachablem-yogi.streamlit.app/"
 st.write(f"YOGI: [Enlace]({url})")
 
 #3
 st.subheader("Análisis de sentimiento")
 image = Image.open('txt_to_audio.png')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos análisis de sentimientos a partir de expresiones.") 
 url = "https://sentimientos-1.streamlit.app/"
 st.write(f"Análisis de sentimiento: [Enlace]({url})")
  
 #4 
 st.subheader("Red Neuronal Basica")
 image = Image.open('OIG8.jpg')
 st.image(image, width=200)
 st.write("En la siguiente veremos una aplicación que utiliza las RNN en predicción de secuencias temporales.") 
 url = "https://rnnbasica.streamlit.app/"
 st.write(f"Red Neuronal Básica: [Enlace]({url})")

 #5
 st.subheader("Reconocimiento optico de caracteres")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos cómo se usa el Reconocimiento Óptico de caracteres OCR en audio.") 
 url = "https://ocr-audioo.streamlit.app/"
 st.write(f"OCR: [Enlace]({url})")


with col3: 
 #1 
 st.subheader("Reconocimiento optico de caracteres")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que utiliza reconocimiento óptico de caracteres (OCR).") 
 url = "https://opticalcr.streamlit.app/"
 st.write(f"Visión: [Enlace]({url})")

 #2 
 st.subheader("Detector de dígitos escritos a mano")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos la capacidad de ✍️ Detección de Dígitos Escritos a Mano.") 
 url = "https://hzwi7bwfepy6scpu7pradh.streamlit.app/"
 st.write(f"Visión: [Enlace]({url})")

 #3
 st.subheader("Text to Speech")
 image = Image.open('txt_to_audio2.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace usaremos una de las aplicaciones de Inteligencia Artificial conversión de texto a voz") 
 url = "https://text-to-voic.streamlit.app/"
 st.write(f"Text to Speech: [Enlace]({url})")

 #4 
 st.subheader("🔍 Detección de Objetos en Imágenes")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos un 🔍 Detección de Objetos en Imágenes.") 
 url = "https://yolov55.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 #5
 st.subheader("Análisis de Datos")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("En el siguiente enlace veremos cómo se pueden analizar datos utilizando agentes.") 
 url = "https://dataagentt.streamlit.app/"
 st.write(f"Datos: [Enlace]({url})")



with col4: 
 #1
 st.subheader("Convoluciones")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace explora cómo los filtros convolucionales transforman imágenes.") 
 url = "https://convoluciones.streamlit.app/"
 st.write(f"Convoluciones: [Enlace]({url})")

 #2
 st.subheader("Sistema Ciberfísico")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico (ChatGPT).") 
 url = "https://chatgptexploring.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 #3
 st.subheader("Sistema Ciberfísico")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico (ChatAnthropic).") 
 url = "https://chatbot-antropic.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")

 #4
 st.subheader("Generación en Contexto (RAG)")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://chatpdefe.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")
  
 #5
 st.subheader("Autoencoder Interactivo")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación Variational Autoencoder interactiva para explorar y generar dígitos.") 
 url = "https://aevminists.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")



