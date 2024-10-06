import requests
import json

# This module is not done yet

configPath = 'config.json'

with open(configPath, 'r') as file:
    configData = json.load(file)

def getWeatherForCity():
    userCity = configData["openWeather"]["city"]
    userKey = configData["openWeather"]["apiKey"]

    url = f"https://api.openweathermap.org/data/2.5/weather?q={userCity}&appid={apiKey}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return 'Failed to retrieve data'
