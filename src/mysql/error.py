"""Modules to handle a MySQL error."""

from __future__ import annotations

from logging import error
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mysql.connector import Error


def error_mysql(e: Error | AttributeError, msg: str) -> None:
    """Raise error with custom message."""
    error(f"{msg}\nTYPE: {type(e)}\nERROR: {e}")
