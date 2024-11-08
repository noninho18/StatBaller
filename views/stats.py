import ast
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Player stats and comparison")

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

first_player_position = player_options[0].split(" - ")[1]
stats_options = (
    ['Overall', 'Goalkeeper', 'Advanced Goalkeeper', 'Defensive', 'Creativity', 'Passing', 'PassTypes', 'Shooting', 'Possession', 'PlayingTime']
)
selected_stats = st.selectbox("Select the type of stat for all players", stats_options)

def get_player_stats(filepath, player_name):
    stats = pd.read_csv(filepath)
    player_stats = stats[stats['Player'] == player_name]
    if not player_stats.empty:
        if 'Comp' in player_stats.columns:
            stat_columns = [col for col in player_stats.columns if col not in ['Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born']]
        else:
            stat_columns = [col for col in player_stats.columns if col not in ['Player', 'Nation', 'Pos', 'Squad', 'Age', 'Born']]
        
        percentiles = stats[stat_columns].apply(calculate_rank)
        player_percentiles = percentiles[stats['Player'] == player_name].iloc[0] if not player_stats.empty else []
        return player_percentiles, stat_columns
    else:
        return None, None

def get_player_data(selected_player, selected_stats, player_idx):
    if (selected_stats == 'Goalkeeper' or selected_stats == 'Advanced Goalkeeper') and selected_player.split(" - ")[1] != 'GK':
        st.write(f"Selected stat type '{selected_stats}' is only available for goalkeepers.")
        return None, None, None
    filepath = "./Data/"
    player_name = selected_player.split(" - ")[0]
    player_born = int(selected_player.split(" - ")[2])

    player_info = player_csv[(player_csv['Player'] == player_name) & (player_csv['Born'] == player_born)]
    player_info_seasons = player_info['Seasons'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
    player_seasons = player_info_seasons.iloc[0] if not player_info.empty else {}

    season_select = st.selectbox(
        "Select a season",
        list(player_seasons.keys()),
        key=f"season_{selected_player}_{selected_stats}_{player_idx}"
    )

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
    
    try:
        stats = pd.read_csv(filepath)
        player_stats = stats[stats['Player'] == player_name]
        stat_columns = [col for col in player_stats.columns if col not in ['Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', 'Club']]
        
        def calculate_rank(series):
            series_numeric = pd.to_numeric(series, errors='coerce')
            zero_like_mask = series_numeric.fillna(0).abs() < 0.01
            rank_series = series_numeric.rank(method="min", ascending=False)
            rank_series[zero_like_mask] = rank_series.max() + 1
            max_rank = rank_series.max()
            return (max_rank - rank_series) / max_rank * 100
        
        percentiles = stats[stat_columns].apply(calculate_rank)
        player_percentiles = percentiles[stats['Player'] == player_name].iloc[0] if not player_stats.empty else []
        return player_percentiles, stat_columns, player_name
    except FileNotFoundError:
        st.write("File not found. Please check the path.")
        return None, None, None

columns = st.columns(3)

players_data = []
colors = ['blue', 'orange', 'green']

for i in range(3):
    with columns[i]:
        selected_player = st.selectbox(f"Select player {i + 1}", player_options, index=None, placeholder="Choose a player", key=f"player_select_{i}")
        
        if selected_player:
            player_percentiles, stat_columns, player_name = get_player_data(selected_player, selected_stats, i)
            
            if player_percentiles is not None:
                players_data.append((player_percentiles, stat_columns, player_name, colors[i]))

if len(players_data) > 0:
    if stat_columns is None:
        st.write("No stats available for the selected players.")
        st.stop()
    else:
        num_vars = len(stat_columns)
        angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
        angles += angles[:1]

        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
        ax.set_theta_offset(np.pi / 2)
        ax.set_theta_direction(-1)

        for percentiles, columns, name, color in players_data:
            player_values = percentiles.tolist() + percentiles.tolist()[:1]
            ax.plot(angles, player_values, color=color, linewidth=2, label=name)
            ax.fill(angles, player_values, color=color, alpha=0.25)

        ax.set_yticks([20, 40, 60, 80, 100])
        ax.set_yticklabels(['20', '40', '60', '80', '100'])
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(stat_columns, fontsize=10)

        plt.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))
        st.pyplot(fig)