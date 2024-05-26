from django.urls import path, include
from rest_framework import routers

from weather.views import WeatherViewSet


router = routers.DefaultRouter()
router.register("weather", WeatherViewSet)


urlpatterns = [
    path("api/", include(router.urls))
]

app_name = "weather"
