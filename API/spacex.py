import requests

# Number of dragons in space
def activeDragons():
    url = "https://api.spacexdata.com/v4/dragons"
    
    response = requests.get(url)

    if response.status_code == 200:
        dragonData = response.json()
        activeDragons = [dragon for dragon in dragonData if dragon['active']]
        return activeDragons
    else:
        return "Failed to retrieve data"

# Dragon names
def dragonNames():
    dragons = activeDragons()
    if isinstance(dragons, list):
        dragonNames = [dragon['name'] for dragon in dragons]
        return dragonNames
    else:
        return "Failed to retrieve dragon names"

# Get next launch
def nextLaunchUTC():
    url = "https://api.spacexdata.com/v4/launches/next"
    response = requests.get(url)

    if response.status_code == 200:
        nextLaunch = response.json()
        launchDate = nextLaunch['date_utc']
        return launchDate
    else:
        return "Failed to retrieve data"
