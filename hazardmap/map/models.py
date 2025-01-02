from django.db import models

class City(models.Model):
    name = models.CharField(max_length=255)
    lat_center = models.FloatField()
    lon_center = models.FloatField()