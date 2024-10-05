import requests
import json

configPath = 'config.json'

with open(configPath, 'r') as file: 
    configData = json.load(file)

apiKey = configData["nasa"]["apiKey"]
#APOD
def APOD():
    url = f'https://api.nasa.gov/planetary/apod?api_key={apiKey}'

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else: 
        return 'Failed to retrieve data'

#Earth
def Earth():
    lat = configData["nasa"]["Earth"]["latitude"]
    lon = configData["nasa"]["Earth"]["longitude"]
    
    if lat and lon:
        url = f'https://api.nasa.gov/planetary/earth/imagery?lon={lon}&lat={lat}&api_key={apiKey}'
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else: 
            return 'Failed to retirieve data'

