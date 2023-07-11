from django.db import models
import time


class Temperature(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    value = models.FloatField(float)

    def __str__(self) -> str:
        return f"at {self.timestamp} the temperature is {self.value}"
