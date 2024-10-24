import streamlit as st
import pandas as pd

from mplsoccer import VerticalPitch


st.title("Stats")
st.subheader("Filter the nation")

# Example: Display a vertical pitch after filtering (for demonstration purposes)
pitch = VerticalPitch(pitch_type='statsbomb', half=True)
fig, ax = pitch.draw(figsize=(10, 10))
st.pyplot(fig)

