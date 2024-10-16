from utils.extraction.extractStats import scrape_data, scrape_commented_data
from utils.csv.to_csv import into_csv, combine_csv

def data_to_csv(folder, leagues, columns, filename):
    league_data = []
    for league_name, url in leagues.items():
        print(f"Scraping {league_name}...")
        if league_name == 'Champions_League':
            columns.remove('Comp')
            data = scrape_commented_data(url, columns)
        else: 
            data = scrape_data(url, columns)
        print(f"{league_name} scraped successfully with {len(data)} rows.")
        league_data.append(data)
        print(data)
        into_csv(data, f"{league_name}_"+filename+"_stats.csv", folder)

    #combine_csv(league_data, filename+'_league_stats.csv', folder)

def basic_stats_scrape():
    folder = "Data/basic_stats"

    leagues = {
        'Top_5_Leagues' : 'https://fbref.com/en/comps/Big5/stats/players/Big-5-European-Leagues-Stats',
        'Champions_League' : 'https://fbref.com/en/comps/8/stats/Champions-League-Stats'
    }
    
    columns = [
        'Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', 'MatchesPlayed', 'Starts', 
        'Min', '90s', 'Goals', 'Assists', 'G+A', 'G-PK', 'PK', 'PKattempted', 'CardY', 'CardR', 
        'xG', 'npxG', 'xAG', 'npxG+xAG', 'PrgCarries', 'PrgPasses', 'PrgReceived', 
        'G/90', 'A/90', 'G+A/90', 'G-PK/90', 'G+A-PK/90', 'xG/90', 'xAG/90', 
        'xG+xAG/90', 'npxG/90', 'npxG+xAG/90', 'Matches'
    ]

    data_to_csv(folder, leagues, columns,"Basic")

def GK_stats_scrape():
    folder = "Data/gk_stats"

    leagues = {
        'Top_5_Leagues' : 'https://fbref.com/en/comps/Big5/keepers/players/Big-5-European-Leagues-Stats',
        'Champions_League' : 'https://fbref.com/en/comps/8/keepers/Champions-League-Stats'
    }

    columns = [
        'Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', 'MatchesPlayed', 'Starts', 
        'Min', '90s', 'GoalsConceded', 'GoalsConceded90', 'SoTAgainst', 'Saves', 'Saves%', 
        'W', 'D', 'L', 'CleanSheet', 'CleanSheet%', 'PKatt', 'PKConcede', 'PKSaved', 'PKMissed', 'PKSaved%', 'Matches'
    ]
    
    data_to_csv(folder, leagues, columns,"GK")

def GK_adv_stats_scrape():
    folder = "Data/gk_advanced_stats"

    leagues = {
        'Top_5_Leagues' : 'https://fbref.com/en/comps/Big5/keepersadv/players/Big-5-European-Leagues-Stats',
        'Champions_League' : 'https://fbref.com/en/comps/8/keepersadv/Champions-League-Stats'
    }

    columns = [
        'Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s', 'GoalsConceded', 'PKConceded', 'GoalsFK', 'GoalsCorner', 'CSC', 'PSxG', 'PSxG/SoT', 
        'PSxG+/-', 'PSxG/90', 'LaunchCompleted', 'LaunchAttempted', 'LaunchCompleted%', 'PassAttempted', 
        'ThrowAttempted', "% of throws", 'PassAvgLen', 'GoalKicksAtt', '% of GoalKicks(+35yards)', 'GoalKicksAvgLen', 
        'OppCrosses', 'CrossesStopped', 'Stp%', 'NbrActionSweeper', 'NbrActionSweeper/90', 'AvgLenFromGoalLine', 'Matches'
    ]
    
    data_to_csv(folder, leagues, columns,"GK_Advanced")