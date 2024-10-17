import re
import time

from utils.extraction.extractStats import scrape_data, scrape_commented_data
from utils.csv.to_csv import into_csv, combine_csv

def data_to_csv(leagues, columns, filename):
    league_data = []
    for league_name, url in leagues.items():
        folder = "Data/"
        year = re.search(r"\d{4}-\d{4}", url)
        if year == None:
            if 'Copa-America' in url :
                folder+= "Int_comps/CopaAmerica2024/"
            elif 'UEFA-Euro' in url :
                folder+= "Int_comps/EURO_2024/"
            elif 'World-Cup' in url :
                folder+= "Int_comps/WC_2022/"
            elif 'Brasil2024' in league_name:
                folder+= "2024/"+filename
            elif 'Brasil2023' in league_name:
                folder+= "2023/"+filename
            else:    
                folder+= "2024-2025/"+filename
        else :
            folder+= year.group()+"/"+filename
        print(f"Scraping {league_name}...")
        if 'Top_5_Leagues' not in league_name:
            if 'Comp' in columns:
                columns.remove('Comp')
            if 'CopaAmerica' in league_name or 'Euro2024' in league_name or 'WorldCup' in league_name:
                if 'Nation' in columns:
                    columns.remove('Nation')
                if 'WorldCup' in league_name and "GK_Advanced" not in filename:
                    columns = columns[:5] + ['Club'] + columns[5:]
            data = scrape_commented_data(url, columns)
        else: 
            data = scrape_data(url, columns)
        if league_name[-1] in '13':
            league_name = league_name[:-1]
        print(f"{league_name} scraped successfully with {len(data)} rows.")
        league_data.append(data)
        print(data)
        into_csv(data, f"{league_name}_"+filename+"_stats.csv", folder)
        time.sleep(20)

def merge_data(leagues, columns, filename):

    combine_csv(league_data, filename+'_stats.csv', folder)

def basic_stats_scrape():

    leagues = {
        'Top_5_Leagues' : 'https://fbref.com/en/comps/Big5/stats/players/Big-5-European-Leagues-Stats',
        # 'Top_5_Leagues1' :'https://fbref.com/en/comps/Big5/2023-2024/stats/players/2023-2024-Big-5-European-Leagues-Stats',
        # 'Top_5_Leagues3' :'https://fbref.com/en/comps/Big5/2022-2023/stats/players/2022-2023-Big-5-European-Leagues-Stats',
        'Primeira_Liga':'https://fbref.com/en/comps/32/stats/Primeira-Liga-Stats',
        # 'Primeira_Liga1': 'https://fbref.com/en/comps/32/2023-2024/stats/2023-2024-Primeira-Liga-Stats',
        # 'Brasil2024SerieA':'https://fbref.com/en/comps/24/stats/Serie-A-Stats',
        # 'Brasil2023SerieA':'https://fbref.com/en/comps/24/2023/stats/2023-Serie-A-Stats',
        'Belgian_Pro_League':'https://fbref.com/en/comps/37/stats/Belgian-Pro-League-Stats',
        # 'Belgian_Pro_League1':'https://fbref.com/en/comps/37/2023-2024/stats/2023-2024-Belgian-Pro-League-Stats',
        'Champions_League' : 'https://fbref.com/en/comps/8/stats/Champions-League-Stats',
        # 'Champions_League1': 'https://fbref.com/en/comps/8/2023-2024/stats/2023-2024-Champions-League-Stats',
        # 'Champions_League3':'https://fbref.com/en/comps/8/2022-2023/stats/2022-2023-Champions-League-Stats',
        'Europa_League' : 'https://fbref.com/en/comps/19/stats/Europa-League-Stats'
        # 'Europa_League1' :'https://fbref.com/en/comps/19/2023-2024/stats/2023-2024-Europa-League-Stats',
        # 'Europa_League3' :'https://fbref.com/en/comps/19/2022-2023/stats/2022-2023-Europa-League-Stats',
        # 'CopaAmerica2024' : 'https://fbref.com/en/comps/685/stats/Copa-America-Stats',
        # 'Euro2024':'https://fbref.com/en/comps/676/stats/UEFA-Euro-Stats',
        # 'WorldCup2022':'https://fbref.com/en/comps/1/stats/World-Cup-Stats'
    }
    
    columns = [
        'Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', 'MatchesPlayed', 'Starts', 
        'Min', '90s', 'Goals', 'Assists', 'G+A', 'G-PK', 'PK', 'PKattempted', 'CardY', 'CardR', 
        'xG', 'npxG', 'xAG', 'npxG+xAG', 'PrgCarries', 'PrgPasses', 'PrgReceived', 
        'G/90', 'A/90', 'G+A/90', 'G-PK/90', 'G+A-PK/90', 'xG/90', 'xAG/90', 
        'xG+xAG/90', 'npxG/90', 'npxG+xAG/90', 'Matches'
    ]

    data_to_csv(leagues, columns,"Basic")

def GK_stats_scrape():

    leagues = {
        'Top_5_Leagues' : 'https://fbref.com/en/comps/Big5/keepers/players/Big-5-European-Leagues-Stats',
        # 'Top_5_Leagues1' :'https://fbref.com/en/comps/Big5/2023-2024/keepers/players/2023-2024-Big-5-European-Leagues-Stats',
        # 'Top_5_Leagues3' :'https://fbref.com/en/comps/Big5/2022-2023/keepers/players/2022-2023-Big-5-European-Leagues-Stats',
        'Primeira_Liga':'https://fbref.com/en/comps/32/keepers/Primeira-Liga-Stats',
        # 'Primeira_Liga1': 'https://fbref.com/en/comps/32/2023-2024/keepers/2023-2024-Primeira-Liga-Stats',
        # 'Brasil2024SerieA':'https://fbref.com/en/comps/24/keepers/Serie-A-Stats',
        # 'Brasil2023SerieA':'https://fbref.com/en/comps/24/2023/keepers/2023-Serie-A-Stats',
        'Belgian_Pro_League':'https://fbref.com/en/comps/37/keepers/Belgian-Pro-League-Stats',
        # 'Belgian_Pro_League1':'https://fbref.com/en/comps/37/2023-2024/keepers/2023-2024-Belgian-Pro-League-Stats',
        'Champions_League' : 'https://fbref.com/en/comps/8/keepers/Champions-League-Stats',
        # 'Champions_League1': 'https://fbref.com/en/comps/8/2023-2024/keepers/2023-2024-Champions-League-Stats',
        # 'Champions_League3':'https://fbref.com/en/comps/8/2022-2023/keepers/2022-2023-Champions-League-Stats',
        'Europa_League' : 'https://fbref.com/en/comps/19/keepers/Europa-League-Stats'
        # 'Europa_League1' :'https://fbref.com/en/comps/19/2023-2024/keepers/2023-2024-Europa-League-Stats',
        # 'Europa_League3' :'https://fbref.com/en/comps/19/2022-2023/keepers/2022-2023-Europa-League-Stats',
        # 'CopaAmerica2024' : 'https://fbref.com/en/comps/685/keepers/Copa-America-Stats',
        # 'Euro2024':'https://fbref.com/en/comps/676/keepers/UEFA-Euro-Stats',
        # 'WorldCup2022':'https://fbref.com/en/comps/1/keepers/World-Cup-Stats'
    }

    columns = [
        'Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', 'MatchesPlayed', 'Starts', 
        'Min', '90s', 'GoalsConceded', 'GoalsConceded90', 'SoTAgainst', 'Saves', 'Saves%', 
        'W', 'D', 'L', 'CleanSheet', 'CleanSheet%', 'PKatt', 'PKConcede', 'PKSaved', 'PKMissed', 'PKSaved%', 'Matches'
    ]
    
    data_to_csv(leagues, columns,"GK")

def GK_adv_stats_scrape():

    leagues = {
        'Top_5_Leagues' : 'https://fbref.com/en/comps/Big5/keepersadv/players/Big-5-European-Leagues-Stats',
        # 'Top_5_Leagues1' :'https://fbref.com/en/comps/Big5/2023-2024/keepersadv/players/2023-2024-Big-5-European-Leagues-Stats',
        # 'Top_5_Leagues3' :'https://fbref.com/en/comps/Big5/2022-2023/keepersadv/players/2022-2023-Big-5-European-Leagues-Stats',
        'Primeira_Liga':'https://fbref.com/en/comps/32/keepersadv/Primeira-Liga-Stats',
        # 'Primeira_Liga1': 'https://fbref.com/en/comps/32/2023-2024/keepersadv/2023-2024-Primeira-Liga-Stats',
        # 'Brasil2024SerieA':'https://fbref.com/en/comps/24/keepersadv/Serie-A-Stats',
        # 'Brasil2023SerieA':'https://fbref.com/en/comps/24/2023/keepersadv/2023-Serie-A-Stats',
        'Belgian_Pro_League':'https://fbref.com/en/comps/37/keepersadv/Belgian-Pro-League-Stats',
        # 'Belgian_Pro_League1':'https://fbref.com/en/comps/37/2023-2024/keepersadv/2023-2024-Belgian-Pro-League-Stats',
        'Champions_League' : 'https://fbref.com/en/comps/8/keepersadv/Champions-League-Stats',
        # 'Champions_League1': 'https://fbref.com/en/comps/8/2023-2024/keepersadv/2023-2024-Champions-League-Stats',
        # 'Champions_League3':'https://fbref.com/en/comps/8/2022-2023/keepersadv/2022-2023-Champions-League-Stats',
        'Europa_League' : 'https://fbref.com/en/comps/19/keepersadv/Europa-League-Stats'
        # 'Europa_League1' :'https://fbref.com/en/comps/19/2023-2024/keepersadv/2023-2024-Europa-League-Stats',
        # 'Europa_League3' :'https://fbref.com/en/comps/19/2022-2023/keepersadv/2022-2023-Europa-League-Stats',
        # 'CopaAmerica2024' : 'https://fbref.com/en/comps/685/keepersadv/Copa-America-Stats',
        # 'Euro2024':'https://fbref.com/en/comps/676/keepersadv/UEFA-Euro-Stats',
        # 'WorldCup2022':'https://fbref.com/en/comps/1/keepersadv/World-Cup-Stats'
    }

    columns = [
        'Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s', 'GoalsConceded', 'PKConceded', 'GoalsFK', 'GoalsCorner', 'CSC', 'PSxG', 'PSxG/SoT', 
        'PSxG+/-', 'PSxG/90', 'LaunchCompleted', 'LaunchAttempted', 'LaunchCompleted%', 'PassAttempted', 
        'ThrowAttempted', "% of throws", 'PassAvgLen', 'GoalKicksAtt', '% of GoalKicks(+35yards)', 'GoalKicksAvgLen', 
        'OppCrosses', 'CrossesStopped', 'Stp%', 'NbrActionSweeper', 'NbrActionSweeper/90', 'AvgLenFromGoalLine', 'Matches'
    ]
    
    data_to_csv(leagues, columns,"GK_Advanced")