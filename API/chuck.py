import requests

def chuckJoke():
    response = requests.get("https://api.chucknorris.io/jokes/random")

    if response.status_code == 200:
        return response.json()["value"]
    else: 
        return 'Failed to retrieve data'