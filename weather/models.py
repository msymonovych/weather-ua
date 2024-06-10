from django.db import models


class WeatherRecord(models.Model):
    date = models.DateField(unique=True)
    temperature = models.FloatField()
    description = models.CharField(max_length=100)
    precipitation = models.FloatField()

    def __str__(self):
        return f"{self.date} - {self.temperature}°C"
