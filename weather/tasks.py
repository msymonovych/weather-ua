from celery import shared_task

from weather.utils import get_weather, WeatherRecordDataclass
from weather.models import WeatherRecord


def update_or_create_record(record: WeatherRecordDataclass):
    if WeatherRecord.objects.filter(date=record.date).exists():
        WeatherRecord.objects.filter(date=record.date).update(
            date=record.date,
            temperature=record.temperature,
            description=record.description,
            precipitation=record.precipitation,
        )
    else:
        WeatherRecord.objects.create(
            date=record.date,
            temperature=record.temperature,
            description=record.description,
            precipitation=record.precipitation,
        )


@shared_task
def get_today_weather():
    record = get_weather()
    update_or_create_record(record[0])


@shared_task
def get_weather_for_five_days():
    records = get_weather(days=5)
    for record in records:
        update_or_create_record(record)
