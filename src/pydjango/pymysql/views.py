"""Views for PyMySQL."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Employee


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    """Response index."""
    return render(request, "index.html")


def employees(request: HttpRequest) -> HttpResponse:
    """Response employees."""
    emps = Employee.objects
    template = loader.get_template("pymysql/index.html")
    context = {"employees": emps}
    return HttpResponse(template.render(context, request))


def employee(request: HttpRequest, employee_id: int) -> HttpResponse:
    """Response employee."""
    emp = Employee.objects.get(id=employee_id)
    template = loader.get_template("pymysql/employee.html")
    context = {"employee": emp}
    return HttpResponse(template.render(context, request))
