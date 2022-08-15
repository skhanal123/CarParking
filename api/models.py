from django.db import models

# This model class is used to create parkingrate database
class parkingRate(models.Model):
    days = models.CharField(max_length = 200)
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    tz = models.CharField(max_length = 200)
    price = models.IntegerField()