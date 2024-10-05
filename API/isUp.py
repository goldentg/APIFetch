import requests
import json

configPath = 'config.json'


with open(configPath, 'r') as file:
    configData = json.load(file)


def isWebsiteUp():
    url = configData["WebsitePing"]["URL"]

    response = requests.get(url)

    if response.status_code == 200:
        return True
    else:
        return False