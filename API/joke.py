#RateLimit: 120 requests per min

import requests

def getRandomJoke():
    url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=racist,sexist"

    response = requests.get(url)

    # If successful
    if response.status_code == 200:
        joke_data = response.json()

        # Check if it's a single or two-part joke
        if joke_data["type"] == "single":
            # Single part joke
            print(joke_data["joke"])
        elif joke_data["type"] == "twopart":
            # Two-part joke (setup and delivery)
            print(joke_data["setup"])
            print(joke_data["delivery"])
    else:
        print ("Failed to retrieve joke")