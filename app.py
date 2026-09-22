import streamlit as st
from gtts import gTTS

st.title("Text to Speech Converter")
text = st.text_area("Enter text to convert to speech:")

if st.button("Convert to Speech"):
    if text.strip():
        voix = gTTS(text=text, lang='fr')

        voix.save("output.mp3")
        st.audio("output.mp3", format="audio/mp3")
    else:
        st.warning("Please enter some text to convert.")
