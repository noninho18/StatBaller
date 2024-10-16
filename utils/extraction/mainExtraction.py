import re

from utils.extraction.extractStats import scrape_data, scrape_commented_data
from utils.csv.to_csv import into_csv, combine_csv

def data_to_csv(leagues, columns, filename):
    league_data = []
    for league_name, url in leagues.items():
        folder = "Data/"
        year = re.search(r"\d{4}-\d{4}", url)
        if year == None:
            folder+= "2024-2025/"+filename
        else :
            folder+= year.group()+"/"+filename
        print(f"Scraping {league_name}...")
        if 'Champions_League' in league_name or 'Europa_League' in league_name:
            if 'Comp' in columns:
                columns.remove('Comp')
            data = scrape_commented_data(url, columns)
        else: 
            data = scrape_data(url, columns)
        if league_name[-1] in '123':
            league_name = league_name[:-1]
        print(f"{league_name} scraped successfully with {len(data)} rows.")
        league_data.append(data)
        print(data)
        into_csv(data, f"{league_name}_"+filename+"_stats.csv", folder)

def merge_data(leagues, columns, filename):

    combine_csv(league_data, filename+'_stats.csv', folder)

def basic_stats_scrape():

    leagues = {
        'Top_5_Leagues' : 'https://fbref.com/en/comps/Big5/stats/players/Big-5-European-Leagues-Stats',
        'Champions_League' : 'https://fbref.com/en/comps/8/stats/Champions-League-Stats',
        'Europa_League' : 'https://fbref.com/en/comps/19/stats/Europa-League-Stats',
        'Champions_League1': 'https://fbref.com/en/comps/8/2023-2024/stats/2023-2024-Champions-League-Stats'
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
        'Champions_League' : 'https://fbref.com/en/comps/8/keepers/Champions-League-Stats',
        'Europa_League' : 'https://fbref.com/en/comps/19/keepers/Europa-League-Stats'
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
        'Champions_League' : 'https://fbref.com/en/comps/8/keepersadv/Champions-League-Stats',
        'Europa_League' : 'https://fbref.com/en/comps/19/keepersadv/Europa-League-Stats'
    }

    columns = [
        'Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s', 'GoalsConceded', 'PKConceded', 'GoalsFK', 'GoalsCorner', 'CSC', 'PSxG', 'PSxG/SoT', 
        'PSxG+/-', 'PSxG/90', 'LaunchCompleted', 'LaunchAttempted', 'LaunchCompleted%', 'PassAttempted', 
        'ThrowAttempted', "% of throws", 'PassAvgLen', 'GoalKicksAtt', '% of GoalKicks(+35yards)', 'GoalKicksAvgLen', 
        'OppCrosses', 'CrossesStopped', 'Stp%', 'NbrActionSweeper', 'NbrActionSweeper/90', 'AvgLenFromGoalLine', 'Matches'
    ]
    
    data_to_csv(leagues, columns,"GK_Advanced")