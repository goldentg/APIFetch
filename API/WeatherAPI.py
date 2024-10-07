import requests
import json

configPath = 'config.json'

with open(configPath, 'r') as file:
    configData = json.load(file)

apiKey = configData["openWeather"]["apiKey"]

def getWeatherByCity():
    userCity = configData["openWeather"]["city"]
    url = f"http://api.openweathermap.org/data/2.5/weather?id={userCity}&appid={apiKey}"

    response = requests.get(url)
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.content}")

    if response.status_code == 200:
        data = response.json()
        print(data)
        return data
    else:
        return 'Failed to retrieve data'