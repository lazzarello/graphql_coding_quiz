from django.shortcuts import HttpResponse

def homePageView(request: str) -> HttpResponse:
    return HttpResponse("Hello, World!")
