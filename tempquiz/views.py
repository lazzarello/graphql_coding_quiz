from django.views.generic import TemplateView, ListView
from .models import Temperature

class HomePageView(ListView):
    model = Temperature
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"