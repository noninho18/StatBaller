from utils.extractData import scrape_league_data, combine_csv, into_csv

if __name__ == "__main__":

    leagues = {
        'Ligue 1': 'https://fbref.com/fr/comps/13/stats/Statistiques-Ligue-1',
        'Premier League': 'https://fbref.com/fr/comps/9/stats/Statistiques-Premier-League',
        'La Liga': 'https://fbref.com/fr/comps/12/stats/Statistiques-La-Liga',
        'Serie A': 'https://fbref.com/fr/comps/11/stats/Statistiques-Serie-A',
        'Bundesliga': 'https://fbref.com/fr/comps/20/stats/Statistiques-Bundesliga'
    }
    
    league_data = []

    for league_name, url in leagues.items():
        print(f"Scraping {league_name}...")
        data = scrape_league_data(url)
        print(f"{league_name} scraped successfully with {len(data)} rows.")
        league_data.append(data)
        into_csv(data, f"{league_name}"+"_stats.csv", "DataCSV")

    combine_csv(league_data, 'football_league_stats.csv', "DataCSV")
