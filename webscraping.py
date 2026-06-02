import requests
from bs4 import BeautifulSoup #pip install requests beautifulsoup4
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Beautifulsoup for static html
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

#
# prices = soup.find_all('span', class_='product-price')
#


# Selenium: Dynamic sites | pip install selenium
def Selenium():
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
    driver.get('https://www.as.com')
    time.sleep(3)
    prices = driver.find_elements(By.CLASS_NAME, 'product-price')
    for price in prices:
        print(price.text)
    driver.quit()

