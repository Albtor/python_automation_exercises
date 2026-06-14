from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def selenium_example():
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
    driver.get('https://www.google.com')
    print(driver.title)
    driver.quit()

def filling_forms():
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
    driver.get('https://www.google.com')
    username = driver.find_elements(By.NAME, 'username')
    password = driver.find_elements(By.NAME, 'password')

    username.send_keys('myusername')
    password.send_keys('mypassword')
    password.send_keys(Keys.RETURN)

    login_button = driver.find_elements(By.XPATH, '//button[@type="submit"]')
    login_button.click()
    driver.quit()

def scraping_data():
    driver = driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
    driver.get('https://www.google.com')
    products = driver.find_elements(By.CLASS_NAME, 'product-name') #//*[@id="products"]
    for product in products:
        print(product.text)
    driver.quit()

def automate_login_and_data_submission():
    driver = driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
    driver.get('https://www.marca.com/login')
    username = driver.find_element(By.NAME, 'username')
    password = driver.find_element(By.NAME, 'password')
    username.send_keys('myusername')
    password.send_keys('mypassword')
    password.send_keys(Keys.RETURN)
    time.sleep(2)

    driver.get('https://www.marca.com/feedback')
    feedback_field = driver.find_element(By.NAME, 'feedback')
    submit_button = driver.find_element(By.NAME, 'submit')
    feedback_field.send_keys('This is my feedback: positive')
    submit_button.click()
    time.sleep(2)
    print("Form submitted successfully")
    driver.quit()