"""Urls for PyMySQL."""

from django.urls import path

from . import views

urlpatterns = [
    path("/", views.index, name="index"),
    path("/employee/<int:employee_id>/", views.employee, name="employee"),
    path("/employees/", views.employees, name="employees"),
]
