#http://numbersapi.com/#42
from datetime import datetime
import requests

def onThisDay():
    currentDate = datetime.now().strftime("%m/%d")
    url = f"http://numbersapi.com/{currentDate}/date"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.text
    else:
        return 'Failed to retrieve data'