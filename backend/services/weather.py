import os
import requests

def get_weather(city_name: str) -> str:
    weather_api_key = os.getenv("WEATHER_API_KEY")
    if not weather_api_key:
        return "Weather API key not found. Please set it in .env."

    if not city_name:
        return "Please specify a city to check the weather."

    url = f"http://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={city_name}&aqi=no"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['current']['temp_c']
        description = data['current']['condition']['text']
        return f"The weather in {city_name} is {description} with a temperature of {temp}°C."
    else:
        return "Sorry, I couldn't fetch the weather for that city."
