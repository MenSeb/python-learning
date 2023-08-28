"""Views for PyMySQL."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Employee


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    """Response index."""
    return render(request, "index.html")


def employees(request: HttpRequest) -> HttpResponse:
    """Response employees."""
    context = {"employees": get_list_or_404(Employee)}
    return render(request, "pymysql/employees.html", context)


def employee(request: HttpRequest, employee_id: int) -> HttpResponse:
    """Response employee."""
    context = {"employee": get_object_or_404(Employee, id=employee_id)}
    return render(request, "pymysql/employee.html", context)
