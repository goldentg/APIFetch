import json
from rich.console import Console
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
import API.proxmox

# Initialize the console
console = Console()

# Load the configuration from the config.json file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Collect all panels to be displayed
panels = []

# Add a random joke panel if enabled in the config
if config.get("joke", {}).get("enable", False):
    panels.append(Panel(API.joke.getRandomJoke(), title="Random Joke", border_style="green"))

# Add SpaceX information panel if any SpaceX options are enabled in the config
if config.get("spacex", {}).get("dragonNames", False) or config.get("spacex", {}).get("nextLaunch", False):
    spacex_content = ""

    # Add active dragon names if enabled in the config
    if config.get("spacex", {}).get("dragonNames", False):
        try:
            active_dragons = API.spacex.activeDragons()
            if isinstance(active_dragons, list):
                dragon_names = API.spacex.dragonNames()
                spacex_content += f'There are {len(active_dragons)} active dragons in orbit:\n'
                spacex_content += "\n".join([f"- {name}" for name in dragon_names])
            else:
                console.print(f"[red]Error fetching active dragons: {active_dragons}[/red]")
        except Exception as e:
            console.print(f"[red]Exception occurred while fetching dragons: {e}[/red]")

    # Add next SpaceX launch information if enabled in the config
    if config.get("spacex", {}).get("nextLaunch", False):
        try:
            next_launch = API.spacex.nextLaunchUTC()
            spacex_content += f'\nNext SpaceX launch is scheduled for: {next_launch}'
        except Exception as e:
            spacex_content += f'\n[red]Error fetching next launch: {e}[/red]'

    panels.append(Panel(spacex_content, title="SpaceX", border_style="green"))

# Add "On This Day" information panel if enabled in the config
if config.get("numbersAPI", {}).get("enable", False):
    panels.append(Panel(f'On this day: {API.numbersAPI.onThisDay()}', title="On This Day", border_style="green"))

# Add Pokemon information panel if any Pokemon options are enabled in the config
if config.get("pokemon", {}).get("enable", False) or config["pokemon"].get("SpecificPokemon", {}).get("enable", False):
    pokemon_content = ""

    # Add a random Pokemon if enabled in the config
    if config.get("pokemon", {}).get("enable", False):
        randomPoke = API.pokemon.getRandomPokemon()
        pokeName = randomPoke['name']
        pokemon_content += f"Random Pokemon: {pokeName}\n"

    # Add specific Pokemon information if enabled in the config
    if config["pokemon"].get("SpecificPokemon", {}).get("enable", False):
        pokemon = API.pokemon.getSpecificPokemon()
        if isinstance(pokemon, dict):
            pmonName = pokemon["name"]
            pmonType = pokemon["types"][0]["type"]["name"]
            pokemon_content += f'Your Pokémon Name: {pmonName}\nPokémon Type: {pmonType}\n'
        else:
            pokemon_content += f'{pokemon}\n'

    panels.append(Panel(pokemon_content.strip(), title="Pokemon", border_style="green"))

# Add a Chuck Norris joke panel if enabled in the config
if config.get("chuck", {}).get("enable", False):
    panels.append(Panel(f"Chuck Joke: {API.chuck.chuckJoke()}", title="Chuck Joke", border_style="green"))

# Add website status panel if enabled in the config
if config.get("WebsitePing", {}).get("enable", False):
    website_statuses = API.isUp.checkWebsites()
    status_content = "\n".join([f"{url}: {'🟢' if status else '🔴'}" for url, status in website_statuses.items()])
    panels.append(Panel(status_content, title="Website Status", border_style="green"))

# Add a random coffee panel if enabled in the config
if config.get("coffee", {}).get("enable", False):
    panels.append(Panel(f"Coffee: {API.coffee.randomCoffee()}", title="Coffee", border_style="green"))

# Add NASA APOD panel if enabled in the config
if config.get("nasa", {}).get("APOD", False):
    apodData = API.nasa.APOD()
    if isinstance(apodData, dict):
        apodTitle = apodData.get("title", "No Title")
        apodExplanation = apodData.get("explanation", "No Explanation")
        apodContent = f"Title: {apodTitle}\nExplanation: {apodExplanation}"
    else:
        apodContent = apodData
    panels.append(Panel(apodContent, title="NASA APOD", border_style="green"))

# Add NASA Earth panel if enabled in the config
if config.get("nasa", {}).get("Earth", {}).get("enable", False):
    earthData = API.nasa.Earth()
    if isinstance(earthData, dict):
        earthDate = earthData.get("date", "No Date")
        earthUrl = earthData.get("url", "No URL")
        earthContent = f"Date: {earthDate}\nImage URL: {earthUrl}"
    else:
        earthContent = earthData
    panels.append(Panel(earthContent, title="NASA Earth", border_style="green"))

if config.get("proxmox", {}).get("enable", False):
    proxmox = API.proxmox.ProxmoxAPI.from_config()
    try:
        nodes = proxmox.list_nodes()
        if nodes:
            node_name = nodes[0]['node']  # Use the first node name from the list
            node_status = proxmox.get_node_status(node_name)

            # Debug: print the node status to understand its structure
            #print(json.dumps(node_status, indent=4))  # Temporary debug line

            # Extracting relevant information with fallback values
            cpu_util_percentage = node_status.get('cpu_util', 'N/A')
            mem_util_percentage = node_status.get('mem_util', 'N/A')
            disk_util_percentage = node_status.get('disk_util', 'N/A')
            status = node_status.get('status', 'Unknown')

            load_avg = node_status.get('loadavg', ['N/A', 'N/A', 'N/A'])
            load_avg_str = ', '.join(map(str, load_avg))

            uptime_seconds = node_status.get('uptime', 0)
            uptime_hours = uptime_seconds // 3600

            # Constructing content for Proxmox panel
            proxmox_content = (
                f"Node Name: {node_name}\n"
                f"Status: {status}\n"
                f"CPU Utilization: {cpu_util_percentage:.2f}%\n"
                f"Memory Utilization: {mem_util_percentage:.2f}%\n"
                f"Disk Utilization: {disk_util_percentage:.2f}%\n"
                f"Load Average: {load_avg_str}\n"
                f"Uptime: {uptime_hours} hours\n"
                f"Kernel Version: {node_status.get('current-kernel', 'Unknown')}"
            )
        else:
            proxmox_content = "No nodes available in Proxmox."
    except Exception as e:
        proxmox_content = f"Error fetching Proxmox node status: {e}"

    panels.append(Panel(proxmox_content, title="Proxmox", border_style="green"))

# Display all panels in columns
if panels:
    console.print(Columns(panels))
else:
    console.print("[red]No information to display.[/red]")
