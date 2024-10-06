import json
import API.joke
import API.spacex
import API.numbersAPI
import API.pokemon
import API.chuck
import API.isUp
import API.nasa
import API.coffee

# Load the configuration
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Check and run modules based on config
if config.get("joke", {}).get("enable", False):
    API.joke.getRandomJoke()

if config.get("spacex", {}).get("enable", False):
    # Getting active dragons and printing count
    active_dragons = API.spacex.activeDragons()
    print('There are ' + str(len(active_dragons)) + ' in orbit')

    # Printing dragon names
    dragon_names = API.spacex.dragonNames()
    for name in dragon_names:
        print(name)

if config.get("numbersAPI", {}).get("enable", False):
    print(f'On this day; {API.numbersAPI.onThisDay()}')

if config.get("pokemon", {}).get("enable", False):
    randomPoke = API.pokemon.getRandomPokemon()
    pokeName = randomPoke['name']
    print(f"Random Pokemon: {pokeName}")

    if config["pokemon"].get("SpecificPokemon", {}).get("enable", False):
        # Get specific Pokémon
        pokemon = API.pokemon.getSpecificPokemon()  # Correct function call
        if isinstance(pokemon, dict):  # Ensure we have a valid response
            pmonName = pokemon["name"]
            pmonType = pokemon["types"][0]["type"]["name"]  # Access the first type correctly

            print(f'Your Pokémon Name: {pmonName}')
            print(f'Pokémon Type: {pmonType}')
        else:
            print(pokemon)  # Print the error message if any

if config.get("chuck", {}).get("enable", False):
    print(f"Chuck Joke: {API.chuck.chuckJoke()}")

if config.get("isUp", {}).get("enable", False):
    if API.isUp:
        print("Website is running")
    else:
        print("Your website is down")

if config.get("coffee", {}).get("enable", False):
    print(f"Coffee: {API.coffee.randomCoffee()}")