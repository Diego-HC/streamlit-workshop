import streamlit as st
from gpt import gpt_wrapper_message

"""
# Hola
---

## Subtitulo
"""

st.image("img.png")

prompt = st.text_input("Escribe un mensaje")

if st.button("Enviar"):
    response = gpt_wrapper_message(prompt)
    st.success(f"Respuesta generada: {response}")
