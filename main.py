import streamlit as st

from PIL import Image
from utils.extraction.mainExtraction import *

def scraper():
    basic_stats_scrape()
    GK_stats_scrape()
    GK_adv_stats_scrape()
    Shooting_stats_scrape()
    Passing_stats_scrape()
    PassTypes_stats_scrape()
    Goal_ShotCreation_stats_scrape()
    DefActions_stats_scrape()
    Possession_stats_scrape()
    PlayingTime_stats_scrape()
    Misc_stats_scrape()

def st_interface():

    im = Image.open("images/logo.webp")
    st.set_page_config(
        page_title="StatBaller",
        page_icon=im,
    )
    
    about_page = st.Page(
        page="views/app.py",    
        title="Ask me anything !",
        icon=":material/account_circle:",
        default=True,
    )
    project_1_page = st.Page(
        page="views/stats.py",
        title="Overall stats",
        icon=":material/bar_chart:",
    )
    project_2_page = st.Page(
        page="views/stats2022_2023.py",
        title="2022-2023 Season",
        icon=":material/bar_chart:",
    )
    project_3_page = st.Page(
        page="views/stats2023_2024.py",
        title="2023-2024 Season",
        icon=":material/bar_chart:",
    )
    project_4_page = st.Page(
        page="views/stats2024_2025.py",
        title="2024-2025 Season",
        icon=":material/bar_chart:",
    )
    project_5_page = st.Page(
        page="views/int_comps.py",
        title="Euro, Copa, WC",
        icon=":material/bar_chart:",
    )

    pg = st.navigation(
        {
            "Chatbot": [about_page],
            "Leagues Stats" : [project_1_page, project_2_page, project_3_page, project_4_page],
            "Int. Competition Stats" : [project_5_page]
        }
    )
    st.logo("images/logo.webp", size="large")
    st.sidebar.markdown("Made with ❤️ by noninho18")

    pg.run()

if __name__ == "__main__":
    # scraper()
    st_interface()