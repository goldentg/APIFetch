import sys
import os
from unittest.mock import patch
from API.isUp import isWebsiteUp, checkWebsites

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Mock configuration data
mock_config_data = {
    "WebsitePing": {
        "URLs": [
            "http://google.com",
            "http://bing.com"
        ]
    }
}

@patch('API.isUp.configData', mock_config_data)
def test_isWebsiteUp_success():
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        assert isWebsiteUp("http://google.com") == True

@patch('API.isUp.configData', mock_config_data)
def test_isWebsiteUp_failure():
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 404
        assert isWebsiteUp("https://potatobingus.com/") == False

@patch('API.isUp.configData', mock_config_data)
def test_checkWebsites():
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        expected_status = {
            "http://google.com": True,
            "http://bing.com": True
        }
        assert checkWebsites() == expected_status