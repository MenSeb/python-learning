from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee


# Create your views here.
def index(request):
    """views index"""
    return HttpResponse("Hello Django!")


def employee(request, employee_id):
    emp = Employee.objects.get(id=employee_id)
    return HttpResponse(f"Employee {employee_id}: {emp}")
