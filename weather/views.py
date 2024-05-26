from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from weather.models import WeatherRecord
from weather.serializers import WeatherSerializer


class WeatherViewSet(
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = WeatherRecord.objects.all()
    serializer_class = WeatherSerializer
