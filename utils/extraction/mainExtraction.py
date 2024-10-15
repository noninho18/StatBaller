from utils.extraction.extractStats import scrape_data
from utils.csv.to_csv import into_csv, combine_csv

def data_to_csv(folder, leagues, columns, filename):
    league_data = []
    for league_name, url in leagues.items():
        print(f"Scraping {league_name}...")
        data = scrape_data(url, columns)
        print(f"{league_name} scraped successfully with {len(data)} rows.")
        league_data.append(data)
        print(data)
        into_csv(data, f"{league_name}_"+filename+"_stats.csv", folder)

    combine_csv(league_data, filename+'_league_stats.csv', folder)

def basic_stats_scrape():
    folder = "Data/basic_stats"

    leagues = {
        'Ligue_1': 'https://fbref.com/fr/comps/13/stats/Statistiques-Ligue-1',
        'Premier_League': 'https://fbref.com/fr/comps/9/stats/Statistiques-Premier-League',
        'La_Liga': 'https://fbref.com/fr/comps/12/stats/Statistiques-La-Liga',
        'Serie_A': 'https://fbref.com/fr/comps/11/stats/Statistiques-Serie-A',
        'Bundesliga': 'https://fbref.com/fr/comps/20/stats/Statistiques-Bundesliga'
    }
    
    columns = [
        'Clt', 'Joueur', 'Nation', 'Pos', 'Équipe', 'Âge', 'Naissance', 'MJ', 
        'Titulaire', 'Min', '90', 'Buts', 'PD', 'B+PD', 'B-PénM', 'PénM', 
        'PénT', 'CJ', 'CR', 'xG', 'npxG', 'xAG', 'npxG+xAG', 'PrgC', 
        'PrgP', 'PrgR', 'Buts/90', 'PD/90', 'B+PD/90', 'B-PénM/90', 
        'B+PD-PénM/90', 'xG/90', 'xAG/90', 'xG+xAG/90', 'npxG/90', 'npxG+xAG/90', 'Matchs'
    ]

    data_to_csv(folder, leagues, columns,"Basic")

def GK_stats_scrape():
    folder = "Data/gk_stats"

    leagues = {
        'Ligue_1': 'https://fbref.com/fr/comps/13/keepers/Statistiques-Ligue-1',
        'Premier_League': 'https://fbref.com/fr/comps/9/keepers/Statistiques-Premier-League',
        'La_Liga': 'https://fbref.com/fr/comps/12/keepers/Statistiques-La-Liga',
        'Serie_A': 'https://fbref.com/fr/comps/11/keepers/Statistiques-Serie-A',
        'Bundesliga': 'https://fbref.com/fr/comps/20/keepers/Statistiques-Bundesliga'
    }

    columns = [
        'Clt', 'Joueur', 'Nation', 'Pos', 'Équipe', 'Âge', 'Naissance', 'MJ', 
        'Titulaire', 'Min', '90', 'ButEncaisse', 'ButEncaisse90', 'TCC', 'Arrêts', 'Arrêts%', 
        'V', 'N', 'D', 'CleanSheet', 'CleanSheet%', 'PenTire', 'PenConcede', 'PenArrete', 'PenManques', 'Arrêts%', 'Matchs'
    ]
    
    data_to_csv(folder, leagues, columns,"GK")

def GK_adv_stats_scrape():
    folder = "Data/gk_advanced_stats"

    leagues = {
        'Ligue_1': 'https://fbref.com/fr/comps/13/keepersadv/Statistiques-Ligue-1',
        'Premier_League': 'https://fbref.com/fr/comps/9/keepersadv/Statistiques-Premier-League',
        'La_Liga': 'https://fbref.com/fr/comps/12/keepersadv/Statistiques-La-Liga',
        'Serie_A': 'https://fbref.com/fr/comps/11/keepersadv/Statistiques-Serie-A',
        'Bundesliga': 'https://fbref.com/fr/comps/20/keepersadv/Statistiques-Bundesliga'
    }

    columns = [
        'Clt', 'Joueur', 'Nation', 'Pos', 'Équipe', 'Âge', 'Naissance', '90', 
        'Buts', 'Attendu', 'Degagement', 'Passes', 'Degagements6m', 
        'Centres', 'Libéro', 'ButEncaisse', 'PenConcede', 'ButCF', 'ButCorner', 'CSC', 'PostShotxG', 'PostShotxG/ShotonTarget', 
        'PostShotxG+/-', 'PostShotxG/90', 'GoalKickCompleted', 'GoalKickAttempted', 'GoalKickCompleted%', 'PassAttempted', 
        'ThrowAttempted', "% of throws", 'PassAvgLen', 'GoalKicksAtt', '% of GoalKicks(+35yards)', 'GoalKicksAvgLen', 
        'OppCrosses', 'CrossesStopped', 'Stp%', 'NbrActionLibero', 'NbrActionLibero/90', 'DistMoy', 'Matchs'
    ]
    
    data_to_csv(folder, leagues, columns,"GK_Advanced")