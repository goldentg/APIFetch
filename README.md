# APIFetch

A small CLI tool that displays various data provided from APIs.

---

## Early Development Notice

**Note:** This project is currently in early development. Features and functionality are subject to change. Contributions and feedback are welcome!

## Current Features
- [x] Proxmox API
  - [x] Display summary 
- [x] Website Ping
  - [x] Check the status of defined websites 
- [x] NASA API
  - [x] Image of the Day
  - [x] Earth Imagery
- [x] SpaceX API (API is out of date)
  - [x] Next Launch
  - [x] Dragon Capsules
- [x] Joke API
- [x] Coffee API
- [x] Numbers API
  - [x] On This Day
- [x] Pokemon API
  - [x] Random Pokemon
  - [x] Pokemon by name
- [x] Chuck Norris API 
- [x] Weather API
  - [x] Current Weather by City

### Planned Features
- [ ] UptimeKuma API
- [ ] GitHub API
- [ ] Lastfm API
- [ ] YouTube API
- [ ] Jellyfin API
- [ ] Plex API
- [ ] RSS
- [ ] Ollama query
- [ ] Device Ping
- [ ] Dog API


## Demo
The following is a very early example of the current functionality of the program (Taken: Oct 7 2024). This will be updated as more features are added.
![APIFetch Demo](.github/Oct%207%20Demo.png)

---


## Installation

```bash
# Clone the repository
git clone https://github.com/goldentg/APIFetch.git
cd APIFetch

# Install dependencies
pip install -r requirements.txt

# Configure the config.json file with your API keys/Customizations

# Run the program
python3 Main.py
```

## API Integration Suggestions
If you have suggestions for new API integrations or improvements, please leave them as feature requests in the Issues section of the repository.

## Future Plans
- Add more API integrations
- Add more functionality to existing API integrations
- Add more customization options
- Add more error handling
- Package project for distribution
