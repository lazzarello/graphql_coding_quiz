from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from .models import Temperature

class TemperatureTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.temp = Temperature.objects.create(time="2023-07-07 00:00:00+00:00",
                                              temperature=0.0)

    def test_model_content(self):
        self.assertEqual(self.temp.time, "2023-07-07 00:00:00+00:00")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About page</h1>")