import streamlit as st
st.title("Mon texte to speech")
texte = st.text_area("Écris le texte à transformer en voix")
if st.button("Lire mon texte"):
    st.write(texte)