import requests

def randomCoffee():
    url = "https://coffee.alexflipnote.dev/random.json"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json().get("file")