import ast
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

st.title("Player stats and comparison")

filepath = "./Data/"

dicoStats = {
    'Overall': "_Basic_stats.csv",
    'Goalkeeper': "_GK_stats.csv",
    'Advanced Goalkeeper': "_GK_Advanced_stats.csv",
    'Defensive': "_DefActions_stats.csv",
    'Creativity': "_Goal_ShotCreation_stats.csv",
    'Passing': "_Passing_stats.csv",
    'PassTypes': "_PassTypes_stats.csv",
    'Shooting': "_Shooting_stats.csv",
    'Possession': "_Possession_stats.csv",
    'PlayingTime': "_PlayingTime_stats.csv"
}

player_csv = pd.read_csv('./Data/players.csv')
player_options = [
    f"{row['Player']} - {row['Pos']} - {int(row['Born']) if pd.notna(row['Born']) else 'Unknown'}"
    for _, row in player_csv.iterrows()
]

selected_player = st.selectbox("Select a player", player_options, index=None, placeholder="Choose a player")
if selected_player:
    if selected_player.split(" - ")[1] == "GK":
        stats_options = ['Overall', 'Goalkeeper', 'Advanced Goalkeeper']
    else:
        stats_options = ['Overall', 'Defensive', 'Creativity', 'Passing', 'PassTypes', 'Shooting', 'Possession', 'PlayingTime']
    selected_stats = st.selectbox("Select the type of stat", stats_options)

    player_name = selected_player.split(" - ")[0]
    player_info = player_csv[(player_csv['Player'] == player_name) & (player_csv['Born'] == int(selected_player.split(" - ")[2]))]
    player_info['Seasons'] = player_info['Seasons'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)

    player_seasons = player_info.iloc[0]['Seasons'] if not player_info.empty else {}

    season_select = st.selectbox("Select a season or a competition", list(player_seasons.keys()) if player_seasons else [])
    if season_select == "CopaAmerica2024" or season_select == "EURO 2024" or season_select == "WC 2022":
        if season_select == "CopaAmerica2024":
            filepath += "Int_comps/CopaAmerica2024/CopaAmerica2024"
        elif season_select == "EURO 2024":
            filepath += "Int_comps/EURO_2024/Euro2024"
        else:
            filepath += "Int_comps/WC_2022/WorldCup2022"
        filepath +=  dicoStats[selected_stats]
    else:
        competition_select = st.selectbox("Select a competition", player_seasons[season_select])
        if competition_select in ['Premier League', 'La Liga', 'Serie A', 'Bundesliga', 'Ligue 1']:
            filepath += season_select + "/" + dicoStats[selected_stats][1:-10] + "/" + "Top_5_Leagues" + dicoStats[selected_stats]
        else:
            filepath += season_select + "/" + dicoStats[selected_stats][1:-10] + "/" + competition_select.replace(" ", "_") + dicoStats[selected_stats]
    stats = pd.read_csv(filepath)
    player_stats = stats[stats['Player'] == player_name]

    def calculate_dense_percentile(series):
        dense_rank = series.rank(method="dense", ascending=False)
        max_rank = dense_rank.max()
        return (max_rank - dense_rank) / max_rank * 100 

    if 'Comp' in player_stats.columns:
        stat_columns = [col for col in player_stats.columns if col not in ['Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born']]
    else:
        stat_columns = [col for col in player_stats.columns if col not in ['Player', 'Nation', 'Pos', 'Squad', 'Age', 'Born']]
    percentiles = stats[stat_columns].apply(calculate_dense_percentile)

    player_percentiles = percentiles[stats['Player'] == player_name].iloc[0] if not player_stats.empty else []

    if not player_stats.empty:
        num_vars = len(stat_columns)
        angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
        ax.set_theta_offset(np.pi / 2)
        ax.set_theta_direction(-1)

        ax.plot(angles, player_percentiles, color='blue', linewidth=2, label=player_name)
        ax.fill(angles, player_percentiles, color='blue', alpha=0.25)

        ax.set_yticks([20, 40, 60, 80, 100])
        ax.set_yticklabels(['20', '40', '60', '80', '100'])
        ax.set_xticks(angles)
        ax.set_xticklabels(stat_columns, fontsize=10)

        st.pyplot(fig)
    else:
        st.write(f"No stats available for {player_name} in {season_select}.")

    st.write(f"Player stats for {player_name} in {season_select}")
    st.write(player_stats)