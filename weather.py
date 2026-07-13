#5b5fb11e3e9842bef7b660dbfb0269ab
import requests
from config import weather_api


def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data["cod"] != 200:
        return "Sorry, I couldn't find that city."

    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    return (
        f"The temperature in {city} is {temperature} degrees Celsius. "
        f"The weather is {description}. "
        f"Humidity is {humidity} percent."
    )