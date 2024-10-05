import API.joke
import API.spacex

API.joke.getRandomJoke()

# Getting active dragons and printing count
active_dragons = API.spacex.activeDragons()
print('There are ' + str(len(active_dragons)) + ' in orbit')

# Printing dragon names
dragon_names = API.spacex.dragonNames()
for name in dragon_names:
    print(name)
