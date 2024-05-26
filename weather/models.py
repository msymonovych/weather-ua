from django.db import models


class WeatherRecord(models.Model):
    date = models.DateField()
    temperature = models.IntegerField()
    description = models.CharField(max_length=100)
    precipitation = models.CharField(max_length=100)

    def __str__(self):
        return str(self.date)
