import streamlit as st

from mplsoccer import VerticalPitch

from utils.extraction.mainExtraction import basic_stats_scrape, GK_stats_scrape, GK_adv_stats_scrape

if __name__ == "__main__":
    # basic_stats_scrape()
    GK_stats_scrape()
    # GK_adv_stats_scrape()
    st.title("StatBaller")
    st.subheader("Filter the league")

    # league = st.selectbox('Select ')
    pitch = VerticalPitch(pitch_type='statsbomb', line_zorder=2, pitch_color='#f0f0f0', line_color='black', half=True)
    fig, ax = pitch.draw(figsize=(10, 10))

    st.pyplot(fig)