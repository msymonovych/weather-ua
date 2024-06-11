from django.shortcuts import render
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from weather.models import WeatherRecord
from weather.serializers import WeatherSerializer
from weather.tasks import get_weather_for_five_days, get_today_weather


class WeatherViewSet(
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = WeatherRecord.objects.all()
    serializer_class = WeatherSerializer

    @action(detail=False, methods=["post"], url_path="today")
    def fetch_today_weather(self, reqeust):
        get_today_weather.delay()
        return Response(
            {"status": "Fetching today's weather"},
            status=status.HTTP_200_OK
        )

    @action(detail=False, methods=["post"], url_path="forecast")
    def fetch_weather_for_five_days(self, request):
        get_weather_for_five_days.delay()
        return Response(
            {"status": "Fetching weather for the next five days"},
            status=status.HTTP_200_OK,
        )
