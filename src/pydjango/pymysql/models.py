"""Models for PyMySQL."""

from django.db import models


# Create your models here.
class Employee(models.Model):
    """Model Employee."""

    first_name = models.CharField(max_length=48)
    last_name = models.CharField(max_length=48)
    email = models.CharField(max_length=319)
    phone = models.CharField(max_length=20)

    def __str__(self: "Employee") -> str:
        """Employee string representation."""
        return f"{self.first_name} {self.last_name}"


class Task(models.Model):
    """Model Task."""

    employee = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=50)
    description = models.TextField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()

    def __str__(self: "Task") -> str:
        """Task string representation."""
        return f"{self.title}"

    def is_assign(self: "Task") -> bool:
        """Check if an employee is assigned to the task."""
        return self.employee is not None
