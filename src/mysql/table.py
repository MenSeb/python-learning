"""Modules to handle a MySQL table."""


from __future__ import annotations

from logging import info
from typing import TYPE_CHECKING

from error import error_mysql

from mysql.connector import Error

if TYPE_CHECKING:
    from mysql.connector.cursor import MySQLCursor


def create_table(table: str, schema: str, cursor: MySQLCursor) -> None:
    """Create a MySQL table."""
    try:
        cursor.execute(f"CREATE TABLE {table}{schema}")
        info(f"Table {table} created successfully.")
    except Error as e:
        error_mysql(e, f"Failed to create table {table}.")


def delete_table(table: str, cursor: MySQLCursor) -> None:
    """Delete a MySQL table."""
    try:
        cursor.execute(f"DROP TABLE {table}")
        info(f"Table {table} deleted successfully.")
    except Error as e:
        error_mysql(e, f"Failed to delete table {table}.")


def describe_table(table: str, cursor: MySQLCursor) -> None:
    """Describe a MySQL table."""
    try:
        cursor.execute(f"DESCRIBE {table}")
        info(f"Table {table} described successfully.")
    except Error as e:
        error_mysql(e, f"Failed to describe table {table}.")


def alter_table(table: str, query: str, cursor: MySQLCursor) -> None:
    """Alter a MySQL table."""
    try:
        cursor.execute(f"ALTER TABLE {table} {query}")
        info(f"Table {table} altered successfully.")
    except Error as e:
        error_mysql(e, f"Failed to alter table {table}.")
