from django.db import models

class Satellites(models.Model):
    status = models.CharField(max_length=50)

class Stats(models.Model):
    satellite = models.ForeignKey(Satellites, on_delete=models.CASCADE)
    altitude = models.IntegerField()
    last_updated = models.DateTimeField()