import requests
from bs4 import BeautifulSoup
from bs4 import Comment

def scrape_fbref_data():
    url = 'https://fbref.com/fr/comps/13/stats/Statistiques-Ligue-1'
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

        if rows:
            result = []
            for row in rows:
                result.append(row.get_text(strip=True))
            return result
        else:
            return "No rows found in the table."
    else:
        return "Table not found in the comments."

# Example of how the result looks
row_data = scrape_fbref_data()
for row in row_data:
    print(row)