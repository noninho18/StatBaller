import streamlit as st
import pandas as pd

from mplsoccer import VerticalPitch

st.title("Player stats during the 2023-2024 season")

filepath = "./Data/2023-2024/"

league_options = ['Champions League', 'Europa League', 'Top 5 Leagues', 'Ligue 1', 'Premier League', 'La Liga', 'Bundesliga', 'Serie A', 'Brazilian Serie A', 'Belgian Pro League', 'Primeira Liga']
selected_league = st.selectbox("Select a competition", league_options)

stats_options = ['Overall', 'Goalkeeper', 'Defensive', 'Creativity', 'Passing', 'Shooting', 'Possession']
selected_stats = st.selectbox("Select the type of stats", stats_options)


dico = {'Overall': "_Basic_stats.csv",
        'Goalkeeper': ["_GK_stats.csv","_GK_Advanced_stats.csv"], 
        'Defensive': "_DefActions_stats.csv", 
        'Creativity': "_Goal_ShotCreation_stats.csv", 
        'Passing': "_Passing_stats.csv", 
        'Shooting': "_Shooting_stats.csv", 
        'Possession': "_Possession_stats.csv"
    }

if selected_stats == 'Goalkeeper':
    if selected_league not in league_options[3:-2]:
        gk_stats_file = selected_league.replace(" ", "_") + dico[selected_stats][0]
        gk_advanced_stats_file = selected_league.replace(" ", "_") + dico[selected_stats][1]
        gk_stats_df = pd.read_csv(filepath + dico[selected_stats][0][1:-10] + "/" + gk_stats_file)
        gk_advanced_df = pd.read_csv(filepath + dico[selected_stats][1][1:-10] + "/" + gk_advanced_stats_file)
        merged_df = pd.merge(gk_stats_df, gk_advanced_df, on=['Player', 'Nation', 'Pos', 'Squad', 'Age', 'Born', '90s', 'GoalsConceded'], how='inner')
        st.write(f"Displaying {selected_stats} stats in {selected_league}")
        st.dataframe(merged_df,  use_container_width=True)
    else:
        if selected_league == 'Brazilian Serie A':
            filepath = "./Data/2024/"
            league = 'Brasil2024SerieA'
            gk_stats_file = league + dico[selected_stats][0]
            gk_advanced_stats_file = league + dico[selected_stats][1]
            gk_stats_df = pd.read_csv(filepath + dico[selected_stats][0][1:-10] + "/" + gk_stats_file)
            gk_advanced_df = pd.read_csv(filepath + dico[selected_stats][1][1:-10] + "/" + gk_advanced_stats_file)
            merged_df = pd.merge(gk_stats_df, gk_advanced_df, on=['Player', 'Nation', 'Pos', 'Squad', 'Age', 'Born', '90s', 'GoalsConceded'], how='inner')
            st.write(f"Displaying {selected_stats} stats in {selected_league}")
            st.dataframe(merged_df,  use_container_width=True)
        else:
            league="Top 5 Leagues"
            gk_stats_file = league.replace(" ", "_") + dico[selected_stats][0]
            gk_advanced_stats_file = league.replace(" ", "_") + dico[selected_stats][1]
            gk_stats_df = pd.read_csv(filepath + dico[selected_stats][0][1:-10] + "/" + gk_stats_file)
            gk_advanced_df = pd.read_csv(filepath + dico[selected_stats][1][1:-10] + "/" + gk_advanced_stats_file)
            merged_df = pd.merge(gk_stats_df, gk_advanced_df, on=['Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s', 'GoalsConceded'], how='inner')
            merged_league_df = merged_df[merged_df['Comp'] == selected_league]
            st.write(f"Displaying {selected_stats} stats in {selected_league}")
            st.dataframe(merged_league_df,  use_container_width=True)
else:
    if selected_league not in league_options[3:-2]:
        filepath += dico[selected_stats][1:-10] + "/" + selected_league.replace(" ", "_") + dico[selected_stats]
        stats_df = pd.read_csv(filepath)
        st.write(f"Displaying {selected_stats} stats in {selected_league}")
        st.dataframe(stats_df,  use_container_width=True)
    else: 
        if selected_league == 'Brazilian Serie A':
            filepath = "./Data/2024/"
            league = 'Brasil2024SerieA'
            filepath += dico[selected_stats][1:-10] + "/" + league + dico[selected_stats]
            stats_df = pd.read_csv(filepath)
            st.write(f"Displaying {selected_stats} stats in {selected_league}")
            st.dataframe(stats_df,  use_container_width=True)
        else:
            league="Top 5 Leagues"
            filepath += dico[selected_stats][1:-10] + "/" + league.replace(" ", "_") + dico[selected_stats]
            stats_df = pd.read_csv(filepath)
            league_df = stats_df[stats_df['Comp'] == selected_league]
            st.write(f"Displaying {selected_stats} stats in {selected_league}")
            st.dataframe(league_df,  use_container_width=True)
