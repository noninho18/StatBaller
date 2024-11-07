import os
import pandas as pd
from collections import defaultdict

base_dir = "./Data"

players_data = {}

seasons = ["2022-2023", "2023", "2023-2024", "2024", "2024-2025"]
int_comps_folder = "Int_comps"

def get_player_key(row):
    player = row["Player"]
    born = int(row["Born"]) if pd.notna(row["Born"]) else 0
    return (player, born)

def add_player_info(row, season, competition, use_squad_as_nation=False):
    player_key = get_player_key(row)
    nation = row["Nation"] if "Nation" in row and pd.notna(row["Nation"]) else (row["Squad"] if use_squad_as_nation else None)
    position = row["Pos"]

    if player_key not in players_data:
        players_data[player_key] = {
            "Player": row["Player"],
            "Nation": nation,
            "Pos": position,
            "Squad": row["Squad"],
            "Born": int(row["Born"]) if pd.notna(row["Born"]) else 0,
            "Seasons": defaultdict(set) 
        }
    else:
        if not players_data[player_key]["Nation"] and nation:
            players_data[player_key]["Nation"] = nation

        current_positions = players_data[player_key]["Pos"].split(", ")
        new_positions = position.split(", ")
        if len(new_positions) > len(current_positions):
            players_data[player_key]["Pos"] = position

    players_data[player_key]["Seasons"][season].add(competition)

for season in seasons:
    basic_folder = os.path.join(base_dir, season, "Basic")
    if os.path.exists(basic_folder):
        for filename in os.listdir(basic_folder):
            if filename.endswith(".csv"):
                filepath = os.path.join(basic_folder, filename)
                if "Top_5_Leagues" in filename:
                    df = pd.read_csv(filepath)
                    for _, row in df.iterrows():
                        competition_name = row["Comp"]
                        add_player_info(row, season, competition_name)
                else:
                    competition_name = os.path.splitext(filename)[0].replace("_Basic_stats", "").replace("_", " ")
                    df = pd.read_csv(filepath)
                    for _, row in df.iterrows():
                        add_player_info(row, season, competition_name)

int_comps_path = os.path.join(base_dir, int_comps_folder)
if os.path.exists(int_comps_path):
    for comp_folder in os.listdir(int_comps_path):
        comp_path = os.path.join(int_comps_path, comp_folder)
        for filename in os.listdir(comp_path):
            if filename.endswith(".csv") and "Basic" in filename:
                filepath = os.path.join(comp_path, filename)
                competition_name = comp_folder.replace("_", " ")
                df = pd.read_csv(filepath)
                for _, row in df.iterrows():
                    add_player_info(row, competition_name, competition_name, use_squad_as_nation=True)

output_data = {
    "Player": [],
    "Nation": [],
    "Pos": [],
    "Squad": [],
    "Born": [],
    "Seasons": []
}

for player_key, data in players_data.items():
    output_data["Player"].append(data["Player"])
    output_data["Nation"].append(data["Nation"])
    output_data["Pos"].append(data["Pos"])
    output_data["Squad"].append(data["Squad"])
    output_data["Born"].append(int(data["Born"]))
    output_data["Seasons"].append({season: list(competitions) for season, competitions in data["Seasons"].items()})

output_df = pd.DataFrame(output_data)
output_df.to_csv("./Data/players.csv", index=False)
print("Extraction complete. Data saved to players_with_seasons.csv")