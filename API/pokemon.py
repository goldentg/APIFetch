import requests
import random
import json

configPath = 'config.json'

with open(configPath, 'r') as file:
    configData = json.load(file)

# Get random pokemon
def getRandomPokemon():
    # Get the total number of Pokémon
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100000')
    
    if response.status_code == 200:
        data = response.json()
        # Generate a random index
        randomIndex = random.randint(0, len(data['results']) - 1)
        randomPokemon = data['results'][randomIndex]

        # Fetch more details about the random Pokémon
        pokemonDetailsResponse = requests.get(randomPokemon['url'])
        
        if pokemonDetailsResponse.status_code == 200:
            return pokemonDetailsResponse.json()



# Get specific pokemon
def getSpecificPokemon():
    setPokemon = configData["pokemon"]["SpecificPokemon"]["name"]
    url = f"https://pokeapi.co/api/v2/pokemon/{setPokemon}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return 'Failed to retrieve data'