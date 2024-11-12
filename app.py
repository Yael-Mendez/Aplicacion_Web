import streamlit as st
from gtts import gTTS
#import os

def create_audiobook(text,language,otuput_file,accent):
    tts=gTTS(text=text,lang=language,tld=accent)#Almacena con el nombre que se le dio
    tts.save(otuput_file)

#Titulo de la Aplicacion
st.title("Text2Audio")

#Imput del Texto
text=st.text_area("Introduce el texto aqui:")

#Lista Desplegable para el Idioma
languages={"Español (es)": "es", "Ingles (en)": "en", "Frances (fr)": "fr", "Aleman (de)": "de"}
language=st.selectbox("Selecciona el idioma:", list(languages.keys()))

#Lista Desplegable para el Acento
accents={"com": "Estados Unidos", "co.uk": "Reino Unido", "ca": "Canada", "com.au": "Australia", "co.in": "India"}
accent = st.selectbox("Selecciona el acento:", list(accents.keys()))

#Boton para generar tetx audio
if st.button("Genera Audio"):
    if text:
        output_file="audiolibro.mp3"
        create_audiobook(text, languages[language], output_file, accent)
        st.audio(output_file,format="audio/mp3")
    else:
        st.error("Por favor, introduce un texto.")