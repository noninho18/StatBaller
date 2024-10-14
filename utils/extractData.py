import requests
import os
import pandas as pd
from bs4 import BeautifulSoup
from bs4 import Comment

def scrape_league_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    
    table_html = None
    for comment in comments:
        if 'table' in comment:
            table_html = comment
            break

    if table_html:
        table_soup = BeautifulSoup(table_html, 'html.parser')
        rows = table_soup.find_all('tr')

        data = []

        columns = [
            'Clt', 'Joueur', 'Nation', 'Pos', 'Équipe', 'Âge', 'Naissance', 'MJ', 
            'Titulaire', 'Min', '90', 'Buts', 'PD', 'B+PD', 'B-PénM', 'PénM', 
            'PénT', 'CJ', 'CR', 'xG', 'npxG', 'xAG', 'npxG+xAG', 'PrgC', 
            'PrgP', 'PrgR', 'Buts/90', 'PD/90', 'B+PD/90', 'B-PénM/90', 
            'B+PD-PénM/90', 'xG/90', 'xAG/90', 'xG+xAG/90', 'npxG/90', 'npxG+xAG/90', 'Matchs', 'Player href'
        ]

        if rows:
            result = []
            for row in rows[2:]:
                cells = row.find_all(['th', 'td'])

                if cells[1].text.strip() == "Joueur":
                    continue
                    
                for link in row.find_all('a'):
                    href = link.get('href')
                    break
                player_url = 'https://fbref.com' + str(href)
                row_data = [cell.text.strip() for cell in cells]
                row_data.append(player_url)
                data.append(row_data)

            df = pd.DataFrame(data, columns=columns)
            df['Nation'] = df['Nation'].apply(lambda x: x[-3:].strip())
            df.drop(columns=['Clt','Matchs'], inplace=True)
            return df
        else:
            return "No rows found in the table."
    else:
        return "Table not found in the comments."


def combine_csv(dataframes, filename, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    full_path = os.path.join(folder, filename)
    combined_df = pd.concat(dataframes, ignore_index=True)
    combined_df.to_csv(full_path, index=False)
    print(f"Data saved to {full_path}")

def into_csv(dataframe, filename, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    full_path = os.path.join(folder, filename)
    dataframe.to_csv(full_path, index=False)
    print(f"Data saved to {full_path}")