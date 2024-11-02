import streamlit as st
import pandas as pd
from PIL import Image

from mplsoccer import VerticalPitch

st.title("StatBaller")

bot_image = Image.open("images/logo.webp")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask something about a football player"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = "Lamine Yamal is the young GOAT"
    st.session_state.messages.append({"role": "BallingBot", "content": response})
    with st.chat_message("bot", avatar=bot_image):
        st.markdown(response)

# Example: Display a vertical pitch after filtering (for demonstration purposes)
pitch = VerticalPitch(pitch_type='statsbomb', half=True)
fig, ax = pitch.draw(figsize=(10, 10))
st.pyplot(fig)

