from rest_framework import serializers

from weather.models import WeatherRecord


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherRecord
        fields = ["date", "temperature", "description", "precipitation"]
