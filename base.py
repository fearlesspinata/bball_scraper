from bs4 import BeautifulSoup as bs
import requests
import statistics


def get_url_resp(url):
    session = requests.Session()
    response = session.get(url, timeout=60)

    return response


def create_crawler(response):
    soup = bs(response.content, 'html.parser')
    return soup


def get_all_links(soup):
    all_links = soup.find_all('a', href=True)

    return all_links


resp = get_url_resp('https://basketball-reference.com/leagues/NBA_2018_per_game.html')
soup = create_crawler(resp)
position_tags = soup.find_all('td', {'class': 'center'})

for position in soup.find_all('td', {'class': 'center'}):
    if 'C' in position.text:
        print(position)


