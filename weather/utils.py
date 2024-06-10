import os
from dataclasses import dataclass
import datetime as dt

import requests


API_KEY = os.environ.get("WEATHER_API_KEY")
CITY = "Kyiv"
WEATHER_API_URL = (
    f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&aqi=no&alerts=no"
)


@dataclass
class WeatherRecordDataclass:
    date: dt.date
    temperature: float
    description: str
    precipitation: float


def get_record(data: dict) -> WeatherRecordDataclass:
    return WeatherRecordDataclass(
        date=dt.date.fromisoformat(data["date"]),
        temperature=data["day"]["avgtemp_c"],
        description=data["day"]["condition"]["text"],
        precipitation=data["day"]["totalprecip_mm"],
    )


def get_weather(days: int = 0) -> [WeatherRecordDataclass]:
    response = requests.get(WEATHER_API_URL, params={"q": CITY, "days": days})
    records = response.json()["forecast"]["forecastday"]

    return [get_record(record) for record in records]
