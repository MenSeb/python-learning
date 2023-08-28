"""Contexts for Django."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .models import Navigation

if TYPE_CHECKING:
    from django.http import HttpRequest


def website_settings(request: HttpRequest) -> dict[str, Any]:
    """Context for website."""
    nav_main = Navigation(
        name="main",
        links=[
            {"text": "Home", "url": "/pymysql"},
            {"text": "Employees", "url": "/pymysql/employees"},
        ],
    )
    nav_socials = Navigation(
        name="socials",
        links=[
            {"icon": "github", "text": "Github", "url": "/pymysql"},
            {"icon": "linkedin", "text": "LinkedIn", "url": "/pymysql/employees"},
        ],
    )
    return {
        "site_brand": "PyMySQL",
        "site_description": "Python application made with MySQL and Django",
        "site_keywords": "Python, MySQL, Django",
        "site_title": "PyMySQL Application",
        "nav_main": nav_main,
        "nav_socials": nav_socials,
    }
