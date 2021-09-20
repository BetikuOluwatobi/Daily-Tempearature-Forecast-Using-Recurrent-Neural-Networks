from django.db import models

# Create your models here.
class Temp(models.Model):
  humidity = models.IntegerField()
  bubble_point = models.IntegerField()
  humid_volume = models.IntegerField()
  density = models.IntegerField()