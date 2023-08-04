from django.db import models

class Satellites(models.Model):
    status = models.IntegerField()
    time_since_change = models.DateTimeField()

class Stats(models.Model):
    satellite = models.ForeignKey(Satellites, on_delete=models.CASCADE)
    altitude = models.IntegerField()
    last_updated = models.DateTimeField()