from django.test import TestCase
from django.urls import reverse
from datetime import datetime

from .models import Temperature


class TemperatureTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.temp = Temperature.objects.create(value=0.0)

    def test_model_content(self):
        self.assertEqual(type(self.temp.value), float)
        self.assertEqual(type(self.temp.timestamp), datetime)

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
