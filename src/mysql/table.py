"""Modules to handle a MySQL table."""


from __future__ import annotations

from logging import error, info
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


def delete_table(name: str, cursor: MySQLCursor) -> None:
    """Delete a MySQL table."""
    try:
        cursor.execute(f"DROP TABLE {name}")
        info(f"Table {name} deleted successfully.")
    except Error as e:
        error(f"Failed to delete table {name}.")
        error(e)


def describe_table(name: str, cursor: MySQLCursor) -> None:
    """Describe a MySQL table."""
    try:
        cursor.execute(f"DESCRIBE  {name}")
        info(f"Table {name} described successfully.")
    except Error as e:
        error(f"Failed to describe table {name}.")
        error(e)


def alter_table(name: str, column: str, attr: str, cursor: MySQLCursor) -> None:
    """Alter a MySQL table."""
    try:
        cursor.execute(f"ALTER TABLE {name} MODIFY COLUMN {column} {attr}")
        info(f"Table {name} column {column} attribute {attr} altered successfully.")
    except Error as e:
        error(f"Failed to alter table {name} column {column} attribute {attr}.")
        error(e)
