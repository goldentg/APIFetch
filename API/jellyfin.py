import requests
import json

class JellyfinAPI:
    def __init__(self, config):
        self.baseUrl = config["jellyfin"]["baseUrl"]
        self.apiKey = config["jellyfin"]["apiKey"]
        self.userId = config["jellyfin"]["userId"]
        self.headers = {
            'X-Emby-Token': self.apiKey
        }

    @classmethod
    def fromConfig(cls, configPath='config.json'):
        with open(configPath, 'r') as file:
            config = json.load(file)
        return cls(config)

    def getLibrary(self):
        url = f"{self.baseUrl}/Users/{self.userId}/Items"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def getFormattedLibrary(self):
        libraryData = self.getLibrary()
        items = libraryData.get('Items', [])
        formattedData = "\n".join([f"{item['Name']} ({item['Type']})" for item in items])
        return formattedData

    def getLatestMedia(self):
        url = f"{self.baseUrl}/Users/{self.userId}/Items/Latest"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def getTotalMediaCount(self):
        url = f"{self.baseUrl}/Users/{self.userId}/Items"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            items = response.json().get('Items', [])
            total_count = sum(item.get('ChildCount', 0) for item in items)
            return total_count
        else:
            response.raise_for_status()

    def getFormattedMediaCounts(self):
        libraryData = self.getLibrary()
        items = libraryData.get('Items', [])

        movies = sum(1 for item in items if item['Type'] == 'Movie')
        tvShows = sum(1 for item in items if item['Type'] == 'Series')
        music = sum(1 for item in items if item['Type'] == 'Audio')

        formattedCounts = (
            f"Movies: {movies}\n"
            f"TV Shows: {tvShows}\n"
            f"Music: {music}"
        )
        return formattedCounts

    def getFormattedMediaCounts(self):
        libraryData = self.getLibrary()
        items = libraryData.get('Items', [])

        movies = sum(1 for item in items if item['Type'] == 'Movie')
        tvShows = sum(1 for item in items if item['Type'] == 'Series')
        music = sum(1 for item in items if item['Type'] == 'Audio')

        formattedCounts = (
            f"Movies: {movies}\n"
            f"TV Shows: {tvShows}\n"
            f"Music: {music}"
        )
        return formattedCounts

if __name__ == "__main__":
    jellyfin = JellyfinAPI.fromConfig()
    try:
        formattedCollections = jellyfin.getFormattedMediaCounts()
        print(formattedCollections)
    except Exception as e:
        print(f"Error fetching Jellyfin collections: {e}")