from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee


# Create your views here.
def index(request):
    """views index"""
    return HttpResponse("Hello Django!")


def employee(request, id):
    emp = Employee.objects().get(id=id)
    return HttpResponse(f"Employee {id}: {emp}")
