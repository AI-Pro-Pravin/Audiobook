import streamlit as st
from PyPDF2 import PdfReader
from gtts import gTTS
from io import BytesIO
# Streamlit app layout
st.title("AudioBook: Get your own audiobook by uploading a pdf file")

file  = st.file_uploader('Upload a pdf file to get your audiobook',type = 'pdf')


# Extract the text
if file is not None:
    with st.spinner('Extracting text from pdf...'):
        pdf_reader = PdfReader(file)
        pdf_text=''
        for page in pdf_reader.pages:
            pdf_text+=page.extract_text()

    with st.spinner('Converting text to speech...'):
        sound_file = BytesIO()
        tts = gTTS(text = pdf_text, lang= 'en')
        tts.write_to_fp(sound_file)

    st.write("# Auto-playing Audio!")
    st.audio(sound_file)

    st.download_button(
            label="Download audiobook",
            data=sound_file,
            file_name="audiobook.mp3",
            mime="audio/mp3")
    
    