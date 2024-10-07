import requests
import json

configPath = 'config.json'


with open(configPath, 'r') as file:
    configData = json.load(file)


def isWebsiteUp(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.RequestException:
        return False

def checkWebsites():
    urls = configData["websiteStatus"]["URLs"]
    status = {}
    for url in urls:
        status[url] = isWebsiteUp(url)
    return status