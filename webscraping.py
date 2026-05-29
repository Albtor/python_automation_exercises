import requests
from bs4 import BeautifulSoup #pip install requests beautifulsoup4

def fetch_links(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a',href=True)
        for link in links:
            print(link['href'])
    else:
        print("Failed to retrieve the webpage")

def retrieve_tags(url, tag):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find_all(tag) # class_='article'
        for headline in headlines:
            print(headline.text.strip())
    else:
        print("Failed to retrieve the webpage")


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     fetch_links('https://www.marca.com/')
#     retrieve_tags('https://www.eldia.es/', 'h1')


