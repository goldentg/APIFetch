import API.joke
import API.spacex
import API.numbersAPI
import API.pokemon
import API.chuck
import API.isUp
import API.nasa


API.joke.getRandomJoke()

# Getting active dragons and printing count
active_dragons = API.spacex.activeDragons()
print('There are ' + str(len(active_dragons)) + ' in orbit')

# Printing dragon names
dragon_names = API.spacex.dragonNames()
for name in dragon_names:
    print(name)

print(f'On this day; {API.numbersAPI.onThisDay()}')


randomPoke = API.pokemon.getRandomPokemon()
pokeName = randomPoke['name']
print(f"Random Pokemon: {pokeName}")

# Get specific Pokémon
pokemon = API.pokemon.getSpecificPokemon()  # Correct function call
if isinstance(pokemon, dict):  # Ensure we have a valid response
    pmonName = pokemon["name"]
    pmonType = pokemon["types"][0]["type"]["name"]  # Access the first type correctly

    print(f'Your Pokémon Name: {pmonName}')
    print(f'Pokémon Type: {pmonType}')
else:
    print(pokemon)  # Print the error message if any


print(f"Chuck Joke: {API.chuck.chuckJoke()}")

if API.isUp:
    print("Website is running")
else:
    print("Your website is down")