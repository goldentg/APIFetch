import requests
import json

configPath = 'config.json'

with open(configPath, 'r') as file:
    configData = json.load(file)

apiKey = configData["openWeather"]["apiKey"]

def getWeatherByCity():
    userCity = configData["openWeather"]["cityID"]
    url = f"http://api.openweathermap.org/data/2.5/weather?id={userCity}&appid={apiKey}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Debug line
        # print(data)

        return data
    else:
        return 'Failed to retrieve data'