"""Modules to handle a MySQL query."""

from __future__ import annotations


def query_condition(condition: str | None) -> str:
    """Build MySQL query condition with WHERE."""
    return f"WHERE {condition}" if condition else ""


def query_priority(priority: bool | None) -> str:
    """Build MySQL query priority with LOW_PRIORITY."""
    return "LOW_PRIORITY" if priority else ""


def query_ignore(ignore: bool | None) -> str:
    """Build MySQL query ignore with IGNORE."""
    return "IGNORE" if ignore else ""


def query_limit(limit: int | None) -> str:
    """Build MySQL query limit with LIMIT."""
    return f"LIMIT {limit}" if limit else ""


def query_order(order: str | None) -> str:
    """Build MySQL query order with ORDER BY."""
    return f"ORDER BY {order}" if order else ""


def query_columns(columns: str | None) -> str:
    """Build MySQL query columns or with *."""
    return columns or "*"
