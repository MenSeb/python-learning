"""Models for PyMySQL."""

from __future__ import annotations

from django.db import models


# Create your models here.
class Employee(models.Model):
    """Model Employee."""

    first_name = models.CharField(max_length=48)
    last_name = models.CharField(max_length=48)
    email = models.CharField(max_length=319)
    phone = models.CharField(max_length=20)

    def __str__(self: Employee) -> str:
        """ToString Employee."""
        return f"{self.first_name} {self.last_name}"


class Task(models.Model):
    """Model Task."""

    employee = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=50)
    description = models.TextField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()

    def __str__(self: Task) -> str:
        """ToString Task."""
        return f"{self.title}"

    def is_assign(self: Task) -> bool:
        """Check if an employee is assigned to the task."""
        return self.employee is not None


class Navigation:
    """Model for site navigation."""

    def __init__(self: Navigation, name: str, links: list[dict[str, str]]) -> None:
        """Init Navigation."""
        self.name = name
        self.links = links

    def __repr__(self: Navigation) -> str:
        """Reprensentation of Navigation."""
        return f"{type(self).__name__}({vars(self)})"

    def __str__(self: Navigation) -> str:
        """ToString Navigation."""
        return f"Navigation for {self.name}."


class NavigationSocials(Navigation):
    """Model for socials navigation."""

    def __init__(
        self: NavigationSocials,
        name: str,
        links: list[dict[str, str]],
    ) -> None:
        """Init NavigationSocials."""
        super().__init__(name, links)
