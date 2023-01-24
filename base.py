from bs4 import BeautifulSoup as bs
import requests

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

resp = get_url_resp('https://basketball-reference.com')
soup = create_crawler(resp)
all_links = get_all_links(soup)

for a in all_links:
    print(f"Link found: {a['href']}")
