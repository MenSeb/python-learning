"""Urls."""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/employee/<int:id>/", views.employee, name="employee"),
]
