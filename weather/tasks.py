from celery import shared_task

from weather.utils import get_weather, WeatherRecordDataclass
from weather.models import WeatherRecord


def save_weather_record(record: WeatherRecordDataclass):
    WeatherRecord.objects.update_or_create(
        date=record.date,
        temperature=record.temperature,
        description=record.description,
        precipitation=record.precipitation,
    )


@shared_task
def get_today_weather():
    record = get_weather()
    save_weather_record(record[0])


@shared_task
def get_weather_for_five_days():
    records = get_weather(days=5)
    for record in records:
        save_weather_record(record)
