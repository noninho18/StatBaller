import re
import time

from utils.extraction.extractStats import scrape_data, scrape_commented_data
from utils.csv.to_csv import into_csv, combine_csv

def data_to_csv(leagues, columns, filename):
    league_data = []
    for league_name, url in leagues.items():
        folder = "/app/Data/"
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
                if 'WorldCup' in league_name and ("Basic" in filename or "GK" in filename):
                    columns = columns[:5] + ['Club'] + columns[5:]
            if 'Belgian_Pro_League' in league_name or 'Brasil' in league_name or 'Primeira_Liga' in league_name :
                data = scrape_commented_data(url, columns, True)
            else:
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

def get_urls(url_code):
    return {
        'Top_5_Leagues' : f'https://fbref.com/en/comps/Big5/{url_code}/players/Big-5-European-Leagues-Stats',
        # 'Top_5_Leagues1' :f'https://fbref.com/en/comps/Big5/2023-2024/{url_code}/players/2023-2024-Big-5-European-Leagues-Stats',
        # 'Top_5_Leagues3' :f'https://fbref.com/en/comps/Big5/2022-2023/{url_code}/players/2022-2023-Big-5-European-Leagues-Stats',
        'Primeira_Liga':f'https://fbref.com/en/comps/32/{url_code}/Primeira-Liga-Stats',
        # 'Primeira_Liga1': f'https://fbref.com/en/comps/32/2023-2024/{url_code}/2023-2024-Primeira-Liga-Stats',
        # 'Brasil2024SerieA':f'https://fbref.com/en/comps/24/{url_code}/Serie-A-Stats',
        # 'Brasil2023SerieA':f'https://fbref.com/en/comps/24/2023/{url_code}/2023-Serie-A-Stats',
        'Belgian_Pro_League':f'https://fbref.com/en/comps/37/{url_code}/Belgian-Pro-League-Stats',
        # 'Belgian_Pro_League1':f'https://fbref.com/en/comps/37/2023-2024/{url_code}/2023-2024-Belgian-Pro-League-Stats',
        'Champions_League' : f'https://fbref.com/en/comps/8/{url_code}/Champions-League-Stats',
        # 'Champions_League1': f'https://fbref.com/en/comps/8/2023-2024/{url_code}/2023-2024-Champions-League-Stats',
        # 'Champions_League3':f'https://fbref.com/en/comps/8/2022-2023/{url_code}/2022-2023-Champions-League-Stats',
        'Europa_League' : f'https://fbref.com/en/comps/19/{url_code}/Europa-League-Stats'
        # 'Europa_League1' :f'https://fbref.com/en/comps/19/2023-2024/{url_code}/2023-2024-Europa-League-Stats',
        # 'Europa_League3' :f'https://fbref.com/en/comps/19/2022-2023/{url_code}/2022-2023-Europa-League-Stats',
        # 'CopaAmerica2024' : f'https://fbref.com/en/comps/685/{url_code}/Copa-America-Stats',
        # 'Euro2024':f'https://fbref.com/en/comps/676/{url_code}/UEFA-Euro-Stats',
        # 'WorldCup2022':f'https://fbref.com/en/comps/1/{url_code}/World-Cup-Stats'
    }


def basic_stats_scrape():

    leagues = get_urls("stats")

    columns = [
        'Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', 'MatchesPlayed', 'Starts', 
        'Min', '90s', 'Goals', 'Assists', 'G+A', 'G-PK', 'PK', 'PKattempted', 'CardY', 'CardR', 
        'xG', 'npxG', 'xAG', 'npxG+xAG', 'PrgCarries', 'PrgPasses', 'PrgReceived', 
        'G/90', 'A/90', 'G+A/90', 'G-PK/90', 'G+A-PK/90', 'xG/90', 'xAG/90', 
        'xG+xAG/90', 'npxG/90', 'npxG+xAG/90', 'Matches'
    ]

    data_to_csv(leagues, columns,"Basic")

def GK_stats_scrape():

    leagues = get_urls("keepers")

    columns = [
        'Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', 'MatchesPlayed', 'Starts', 
        'Min', '90s', 'GoalsConceded', 'GoalsConceded90', 'SoTAgainst', 'Saves', 'Saves%', 
        'W', 'D', 'L', 'CleanSheet', 'CleanSheet%', 'PKatt', 'PKConcede', 'PKSaved', 'PKMissed', 'PKSaved%', 'Matches'
    ]
    
    data_to_csv(leagues, columns,"GK")

def GK_adv_stats_scrape():

    leagues = get_urls("keepersadv")

    columns = [
        'Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s', 'GoalsConceded', 'PKConceded', 'GoalsFK', 'GoalsCorner', 'CSC', 'PSxG', 'PSxG/SoT', 
        'PSxG+/-', 'PSxG/90', 'LaunchCompleted', 'LaunchAttempted', 'LaunchCompleted%', 'PassAttempted', 
        'ThrowAttempted', "% of throws", 'PassAvgLen', 'GoalKicksAtt', '% of GoalKicks(+35yards)', 'GoalKicksAvgLen', 
        'OppCrosses', 'CrossesStopped', 'Stp%', 'NbrActionSweeper', 'NbrActionSweeper/90', 'AvgLenFromGoalLine', 'Matches'
    ]
    
    data_to_csv(leagues, columns,"GK_Advanced")

def Shooting_stats_scrape():

    leagues = get_urls("shooting")

    columns = [
        'Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s', 'Goals', 'Shots', 'SoT', 'SoT%', 'Shots/90', 'SoT/90', 'Goals/Shots', 
        'Goals/SoT', 'AvgDist', 'FK', 'PK', 'PKatt', 'xG', 'npxG', 'npxG/Sh', 'G-xG', 'np:G-xG', 'Matches'
    ]
    
    data_to_csv(leagues, columns,"Shooting")

def Passing_stats_scrape():

    leagues = get_urls("passing")

    columns = [
        'Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s', 'PassCompleted', 
        'PassAtt', 'PassCompleted%', 'TotDist', 'PrgDist', 'ShortCmp', 'ShortAtt', 'ShortCmp%',	'MediumCmp',
        'MediumAtt', 'MediumCmp%', 'LongCmp', 'LongAtt', 'LongCmp%', 'Ast',	'xAG', 'xA', 'A-xAG','KeyPasses',
        'FinalThird', 'PassesPenArea',	'CrossPenArea',	'ProgPasses', 'Matches'
    ]
    
    data_to_csv(leagues, columns,"Passing")

def PassTypes_stats_scrape():

    leagues = get_urls("passing_types")

    columns = [
        'Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s', 'PassAtt',
        'Live', 'Dead', 'FK', 'ThroughBalls', 'SideSwitch', 'Cross', 'Throw-Ins', 'Corners', 'InSwingCorner',
        'OutSwingCorner', 'StraightCorner',	'PassesCmp', 'PassOffside', 'PassesBlocked', 'Matches'
    ]
    
    data_to_csv(leagues, columns,"PassTypes")

def Goal_ShotCreation_stats_scrape():

    leagues = get_urls("gca")

    columns = [
        'Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s', 'SCA', 'SCA/90', 
        'SCAPassLive', 'SCAPassDead', 'SCATakeOns', 'SCAShots', 'SCAFoulsDrawn', 'SCADefAction',
        'GCA', 'GCA/90', 'GCAPassLive', 'GCAPassDead','GCATakeOns','GCAShots', 'GCAFoulsDrawn', 'GCADefAction', 'Matches'
    ]
    
    data_to_csv(leagues, columns,"Goal_ShotCreation")

def DefActions_stats_scrape():

    leagues = get_urls("defense")

    columns = [
        'Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s', 'Tackles',	
        'TacklesWon', 'TacklesDef3rd', 'TacklesMid3rd', 'TacklesAtt3rd', 'DribTkl', 'DribTklAtt', 'DribTkl%', 'ChallengesLost',
        'Blocks', 'ShotsBlocked', 'PassesBlocked', 'Int', 'Tkl+Int', 'Clr', 'ErrorsLeadingToShot', 'Matches'
    ]
    
    data_to_csv(leagues, columns,"DefActions")

def Possession_stats_scrape():

    leagues = get_urls("possession")

    columns = [
        'Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s', 'Touches',	
        'TouchesDefPen', 'TouchesDef3rd', 'TouchesMid3rd','TouchesAtt3rd', 'TouchesAttPen', 'LiveTouches',
        'TakeOnsAtt', 'TakeOnsSucc', 'TakeOnsSucc%', 'TakeOnsTkld', 'TakeOnsTkld%',	'Carries',	'CarryTotDist',
        'CarryPrgDist', 'PrgCarries', 'CarriesFinal3rd', 'CarriesPenArea', 'Miscontrols', 'Dispossessed','PassesReceived',	
        'PrgPassesReceived', 'Matches'
    ]
    
    data_to_csv(leagues, columns,"Possession")

def PlayingTime_stats_scrape():

    leagues = get_urls("playingtime")

    columns = [
        'Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', 'MP',	
        'Min', 'Min/MP', 'Min%', '90s', 'Starts','Min/Start', 'MatchesCompleted', 'Subs', 'Min/Sub', 'unusedSub',
        'PointsPerMatch', 'onGoalScored', 'onGoalAgainst', '+/-', '+/-/90', 'On-Off', 'onPitchxG', 'onPitchxGA', 'xG+/-',
        'xG+/-/90',	'xGOn-Off', 'Matches'
    ]
    
    data_to_csv(leagues, columns,"PlayingTime")

def Misc_stats_scrape():

    leagues = get_urls("misc")

    columns = [
        'Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s', 'CrdY', 'CrdR', '2CrdY',
        'Fouls', 'FoulsDrawn', 'Offsides', 'Crosses', 'Interceptions', 'TklWon', 'PKwon', 'PKconceded', 'OG',
        'Recoveries', 'AerialDuelsWon', 'AerialDuelsLost', 'AerialDuelsWon%', 'Matches'
    ]

    data_to_csv(leagues, columns,"Misc")