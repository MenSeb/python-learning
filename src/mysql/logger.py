"""Modules to handle a MySQL error."""

from __future__ import annotations

from logging import INFO, basicConfig, error, info
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mysql.connector import Error


basicConfig(level=INFO)


def error_mysql(e: Error | AttributeError, msg: str) -> None:
    """Output MySQL error with custom message."""
    error(f"{msg}\nTYPE: {type(e)}\nERROR: {e}")


def sucess_mysql(message: str) -> None:
    """Output MySQL success with custom message."""
    info(message)
