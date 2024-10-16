import requests
import pandas as pd
from bs4 import BeautifulSoup
from bs4 import Comment

def scrape_data(url, columns):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table_soup = BeautifulSoup(response.text, 'html.parser')
    rows = table_soup.find_all('tr')

    data = []

    if rows:
        result = []
        for row in rows[2:]:
            cells = row.find_all(['th', 'td'])

            if cells[1].text.strip() == "Player":
                continue

            row_data = [cell.text.strip() for cell in cells]
            data.append(row_data)
 
        df = pd.DataFrame(data, columns=columns)
        df['Nation'] = df['Nation'].apply(lambda x: x[-3:].strip())
        df['Comp'] = df['Comp'].apply(lambda x: " ".join(x.split()[1:]))
        df.drop(columns=['Rk','Matches'], inplace=True)
        return df
    else:
        return "No rows found in the table."

def scrape_commented_data(url,columns): 
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

        if rows:
            result = []
            for row in rows[2:]:
                cells = row.find_all(['th', 'td'])

                if cells[1].text.strip() == "Player":
                    continue

                row_data = [cell.text.strip() for cell in cells]
                data.append(row_data)

            df = pd.DataFrame(data, columns=columns)
            if 'Nation' in df.columns:
                df['Nation'] = df['Nation'].apply(lambda x: x[-3:].strip())
            if 'Club' in df.columns:
                df['Club'] = df['Club'].apply(lambda x: " ".join(x.split()[1:]))
            df['Squad'] = df['Squad'].apply(lambda x: " ".join(x.split()[1:]))
            df.drop(columns=['Rk','Matches'], inplace=True)
            return df
        else:
            return "No rows found in the table."
    else:
        return "Table not found in the comments."