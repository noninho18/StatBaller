import streamlit as st

from utils.extraction.mainExtraction import basic_stats_scrape, GK_stats_scrape, GK_adv_stats_scrape

if __name__ == "__main__":
    basic_stats_scrape()
    # GK_stats_scrape()
    # GK_adv_stats_scrape()
    st.title("StatBaller")
    st.subheader("Filter the league")

    league = st.selectbox('Select ')
