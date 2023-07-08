from django.db import models
import time

class Temperature(models.Model):
    timestamp = models.DateTimeField()
    value = models.FloatField()

    def __str__(self) -> time:
        return str(self.timestamp)