import requests
import json

configPath = 'config.json'

with open(configPath, 'r') as file:
    configData = json.load(file)

apiKey = configData["openWeather"]["apiKey"]

def getWeatherByCity():
    userCity = configData["openWeather"]["cityID"]
    url = f"http://api.openweathermap.org/data/2.5/weather?id={userCity}&appid={apiKey}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Debug line
        # print(data)

        return data
    else:
        return 'Failed to retrieve data'

def formatWeatherData(weather, unit):
    cityName = weather["name"]
    weatherDescription = weather["weather"][0]["description"]

    # Convert from Kelvin to Celsius and Fahrenheit
    weatherTempC = weather["main"]["temp"] - 273.15
    weatherTempF = (weather["main"]["temp"] - 273.15) * 9/5 + 32

    weatherFeelsLikeC = weather["main"]["feels_like"] - 273.15
    weatherFeelsLikeF = (weather["main"]["feels_like"] - 273.15) * 9/5 + 32

    weatherWindSpeed = weather["wind"]["speed"]
    weatherWindSpeedMiles = weatherWindSpeed * 0.000621371

    weatherPressure = weather["main"]["pressure"]
    weatherHumidity = weather["main"]["humidity"]

    if unit == "metric":
        return (
            f"City: {cityName}\n"
            f"Conditions: {weatherDescription}\n"
            f"Temperature: {weatherTempC:.2f}°C\n"
            f"Feels Like: {weatherFeelsLikeC:.2f}°C\n"
            f"Humidity: {weatherHumidity}%\n"
            f"Wind Speed: {weatherWindSpeed} m/s\n"
            f"Pressure: {weatherPressure} hPa"
        )
    else:
        return (
            f"City: {cityName}\n"
            f"Conditions: {weatherDescription}\n"
            f"Temperature: {weatherTempF:.2f}°F\n"
            f"Feels Like: {weatherFeelsLikeF:.2f}°F\n"
            f"Humidity: {weatherHumidity}%\n"
            f"Wind Speed: {weatherWindSpeedMiles:.2f} mph\n"
            f"Pressure: {weatherPressure} hPa"
        )