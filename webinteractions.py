from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def selenium_example():
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
    driver.get('https://www.google.com')
    print(driver.title)
    driver.quit()

def filling_forms():
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
