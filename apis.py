import requests
import schedule
import time

def api_exercise():
    API_KEY = "XXXXXX"
    city = 'Santa Cruz'
    url = f'http://api.opneweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

    response = requests.get(url)
    headers = {'Authorization': 'Bearer XXXXX'}
    if response.status_code == 200:
        data = response.json()
        city_name = data['name']
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        print(f"Weather in {city_name}")
        print(f"Temperature: {temperature}")
        print(f"Description: {description}")
        # print(data)
    else:
        print(f'Failed to retrieve data:{response.status_code}')


def get_weather_automated():
    APIKEY = 'sxxxx'
    city = 'Santa Cruz'
    url = f'http://api.opneweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    headers = {'Authorization': 'Bearer XXXXX'}
    if response.status_code == 200:
        data = response.json()
        city_name = data['name']
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        print(f"Weather in {city_name}, Temperature: {temperature}ºC, Description: {description}")
    else:
        print(f'Failed to retrieve data:{response.status_code}')

    schedule.every(1).hours.do(get_weather_automated)
    while True:
        schedule.run_pending()
        time.sleep(1)
