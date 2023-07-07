from django.db import models
import time

class Temperature(models.Model):
    time = models.DateTimeField()
    temperature = models.FloatField()

    def __str__(self) -> time:
        return str(self.time)