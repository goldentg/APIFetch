import json
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.columns import Columns
import API.joke
import API.spacex
import API.numbersAPI
import API.pokemon
import API.chuck
import API.isUp
import API.nasa
import API.coffee

# Initialize the console
console = Console()

# Load the configuration
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Function to print nicely formatted tables
def print_table(title, headers, rows):
    table = Table(title=title)
    for header in headers:
        table.add_column(header)
    for row in rows:
        table.add_row(*row)
    return table

# Collect all panels
panels = []

# Check and run modules based on config
if config.get("joke", {}).get("enable", False):
    panels.append(Panel(API.joke.getRandomJoke(), title="Random Joke", border_style="green"))

if config.get("spacex", {}).get("dragonNames", False) or config.get("spacex", {}).get("nextLaunch", False):
    spacex_content = ""

    if config.get("spacex", {}).get("dragonNames", False):
        try:
            active_dragons = API.spacex.activeDragons()
            if isinstance(active_dragons, list):
                dragon_names = API.spacex.dragonNames()
                spacex_content += f'There are {len(active_dragons)} active dragons in orbit\n'
                spacex_content += "\n".join([f"- {name}" for name in dragon_names])
            else:
                console.print(f"[red]Error fetching active dragons: {active_dragons}[/red]")
        except Exception as e:
            console.print(f"[red]Exception occurred: {e}[/red]")

    if config.get("spacex", {}).get("nextLaunch", False):
        next_launch = API.spacex.nextLaunchUTC()
        spacex_content += f'\nNext SpaceX launch is scheduled for: {next_launch}'

    panels.append(Panel(spacex_content, title="SpaceX", border_style="green"))

if config.get("numbersAPI", {}).get("enable", False):
    panels.append(Panel(f'On this day: {API.numbersAPI.onThisDay()}', title="On This Day", border_style="green"))

if config.get("pokemon", {}).get("enable", False) or config["pokemon"].get("SpecificPokemon", {}).get("enable", False):
    pokemon_content = ""

    if config.get("pokemon", {}).get("enable", False):
        randomPoke = API.pokemon.getRandomPokemon()
        pokeName = randomPoke['name']
        pokemon_content += f"Random Pokemon: {pokeName}\n"

    if config["pokemon"].get("SpecificPokemon", {}).get("enable", False):
        pokemon = API.pokemon.getSpecificPokemon()
        if isinstance(pokemon, dict):
            pmonName = pokemon["name"]
            pmonType = pokemon["types"][0]["type"]["name"]
            pokemon_content += f'Your Pokémon Name: {pmonName}\nPokémon Type: {pmonType}\n'
        else:
            pokemon_content += f'{pokemon}\n'

    panels.append(Panel(pokemon_content.strip(), title="Pokemon", border_style="green"))

if config.get("chuck", {}).get("enable", False):
    panels.append(Panel(f"Chuck Joke: {API.chuck.chuckJoke()}", title="Chuck Joke", border_style="green"))

if config.get("isUp", {}).get("enable", False):
    status = "Website is running" if API.isUp else "Your website is down"
    panels.append(Panel(status, title="Website Status", border_style="green"))

if config.get("coffee", {}).get("enable", False):
    panels.append(Panel(f"Coffee: {API.coffee.randomCoffee()}", title="Coffee", border_style="green"))

# Display all panels in 3 columns
console.print(Columns(panels, equal=True, expand=True))