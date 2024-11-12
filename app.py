import streamlit as st #importar todas las herramientas necesaria
from gtts import gTTS #importar las herramientas de voz de google
def create_audiobook(text,language,output_file,): #generar apartir del texto un audio 
    tts=gTTS(text= text, lang=language, tld='com') #crea un objeto para obtener una voz a la cual se le asigna un texto el idioma y acento
    tts.save(output_file) #almacena un audio con el nombre que se le asigne
    #Título de la aplicación
st.title("Text2Audio")
text=st.text_area("Introduce el texto aqui:")
# Lista desplegable para el Idioma
languages = {
    "Español (es)": "es",
    "Ingles (en)": "en",
    "Francés (fr)": "fr",
    "Alemán (de)":"de" 
}
language = st.selectbox("selecciona el idioma:", list(languages.keys()))

# Lista desplegable para el acento
accent = {
    "com": "Estados Unidos",
    "co.uk": "Reino Unido",
    "ca": "Canadá",
    "com.au": "Australia",
    "co.in":"India"
}
accent = st.selectbox("Selecciona el acento:", list(accent.keys()))
# Boton para Generar Audiolibro
if st.button("Generar Audiolibro"):
    if text:
        output_file = "audiolibro.mp3"
        create_audiobook(text, languages[language], output_file)
        st.audio(output_file, format="audio/mp3")
else:
    st.error("Por favor, introduce un texto.")