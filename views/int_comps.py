import streamlit as st
import pandas as pd
from mplsoccer import VerticalPitch

st.title("Player stats during international competitions")

filepath = "./Data/Int_comps/"

dicoStats = {
    'Overall': "_Basic_stats.csv",
    'Goalkeeper': ["_GK_stats.csv", "_GK_Advanced_stats.csv"],
    'Defensive': "_DefActions_stats.csv",
    'Creativity': "_Goal_ShotCreation_stats.csv",
    'Passing': "_Passing_stats.csv",
    'PassTypes': "_PassTypes_stats.csv",
    'Shooting': "_Shooting_stats.csv",
    'Possession': "_Possession_stats.csv",
    'PlayingTime': "_PlayingTime_stats.csv"
}

dicoComp = {
   'Copa America 2024': 'CopaAmerica2024',
   'Euro 2024': 'EURO_2024',
   'World Cup 2022': 'WC_2022'
}

league_options = ['Copa America 2024', 'Euro 2024', 'World Cup 2022']
selected_comp = st.selectbox("Select a competition", league_options)

stats_options = ['Overall', 'Goalkeeper', 'Defensive', 'Creativity', 'Passing', 'PassTypes', 'Shooting', 'Possession', 'PlayingTime']
selected_stats = st.selectbox("Select the type of stat", stats_options)

filepath += dicoComp[selected_comp] + "/" + selected_comp.replace(" ", "") 
if selected_stats == 'Goalkeeper':
    comp_df = pd.read_csv(filepath + dicoStats['Goalkeeper'][0])
else:
    comp_df = pd.read_csv(filepath + dicoStats[selected_stats])

squad_options = list(comp_df['Squad'].unique())
selected_squad = st.selectbox("Select a squad", squad_options, index=None, placeholder="Choose a squad")

if selected_squad is not None:
    squad_df = comp_df[comp_df['Squad'] == selected_squad]
    player_options = list(squad_df['Player'].unique())
    selected_player = st.selectbox("Select a player", player_options, index=None, placeholder="Choose a player")

if selected_stats == 'Goalkeeper':

    gk_stats_df = pd.read_csv(filepath + dicoStats['Goalkeeper'][0])
    gk_advanced_df = pd.read_csv(filepath + dicoStats['Goalkeeper'][1])
    merged_df = pd.merge(gk_stats_df, gk_advanced_df, on=['Player', 'Pos', 'Squad', 'Age', 'Born', '90s', 'GoalsConceded'], how='inner')
    
    if selected_squad and selected_player:
        filtered_df = merged_df[(merged_df['Squad'] == selected_squad) & (merged_df['Player'] == selected_player)]
        st.write(f"Displaying {selected_stats} stats in {selected_comp} for {selected_player}")
    elif selected_squad:
        filtered_df = merged_df[merged_df['Squad'] == selected_squad]
        st.write(f"Displaying {selected_stats} stats in {selected_comp} for {selected_squad}")
    else:
        filtered_df = merged_df
        st.write(f"Displaying {selected_stats} stats in {selected_comp}")
    
    st.dataframe(filtered_df, use_container_width=True)

else:
    stats_df = pd.read_csv(filepath + dicoStats[selected_stats])
    
    if selected_squad and selected_player:
        filtered_df = stats_df[(stats_df['Squad'] == selected_squad) & (stats_df['Player'] == selected_player)]
        st.write(f"Displaying {selected_stats} stats in {selected_comp} for {selected_player}")
    elif selected_squad:
        filtered_df = stats_df[stats_df['Squad'] == selected_squad]
        st.write(f"Displaying {selected_stats} stats in {selected_comp} for {selected_squad}")
    else:
        filtered_df = stats_df
        st.write(f"Displaying {selected_stats} stats in {selected_comp}")
    
    st.dataframe(filtered_df, use_container_width=True)
