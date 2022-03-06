from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, I am Amudan")


def hello(request, name):
    return HttpResponse(f"Hi ! {name.capitalize()}")


def test(request):
    return render(request, "htmlpage/hi.html")
