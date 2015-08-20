from django.db import models

class Interval_Counters(models.Model):
    interval_start = models.BigIntegerField()
    interval_stop = models.BigIntegerField()
    count = models.IntegerField(default=0)
    server = models.CharField(max_length=50)
    origin = models.CharField(max_length=150)
    interval_key = models.CharField(max_length=242, primary_key=True)


