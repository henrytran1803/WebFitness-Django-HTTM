from urllib import request

from django.shortcuts import render

# Create your views here.
def index(request):
    return  render(request, "../templates/html/index.html")
