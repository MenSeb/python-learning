from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    """views index"""
    return HttpResponse("Hello Django!")
