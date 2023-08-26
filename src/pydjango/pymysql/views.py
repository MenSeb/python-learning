"""Views for PyMySQL."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Employee


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    """Response index."""
    return render(request, "pymysql/index.html")


def employees(request: HttpRequest) -> HttpResponse:
    """Response employees."""
    context = {"employees": Employee.objects.all()}
    return render(request, "pymysql/employees.html", context)


def employee(request: HttpRequest, employee_id: int) -> HttpResponse:
    """Response employee."""
    context = {"employee": Employee.objects.get(id=employee_id)}
    return render(request, "pymysql/employee.html", context)
