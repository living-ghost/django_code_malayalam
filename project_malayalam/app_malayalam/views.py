from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "home.html")

def contact(request):
    return render(request, "contact.html")

def courses(request):
    return render(request, "courses.html")

def about(request):
    return render(request, "about.html")

def python_chapter_1(request):
    return render(request, "courses/python/python-intro.html")

def python_chapter_2(request):
    return render(request, "courses/python/python-var-data.html")