"""Modules to handle a MySQL table."""


from __future__ import annotations

from typing import TYPE_CHECKING

from logger import error_mysql, sucess_mysql

from mysql.connector import Error

if TYPE_CHECKING:
    from mysql.connector.cursor import MySQLCursor


def create_table(table: str, schema: str, cursor: MySQLCursor) -> None:
    """Create a MySQL table."""
    try:
        cursor.execute(f"CREATE TABLE {table}{schema}")
    except Error as e:
        error_mysql(e, f"Failed to create table {table}.")
    else:
        sucess_mysql(f"Table {table} created successfully.")


def delete_table(table: str, cursor: MySQLCursor) -> None:
    """Delete a MySQL table."""
    try:
        cursor.execute(f"DROP TABLE {table}")
    except Error as e:
        error_mysql(e, f"Failed to delete table {table}.")
    else:
        sucess_mysql(f"Table {table} deleted successfully.")


def describe_table(table: str, cursor: MySQLCursor) -> None:
    """Describe a MySQL table."""
    try:
        cursor.execute(f"DESCRIBE {table}")
    except Error as e:
        error_mysql(e, f"Failed to describe table {table}.")
    else:
        sucess_mysql(f"Table {table} described successfully.")


def alter_table(table: str, query: str, cursor: MySQLCursor) -> None:
    """Alter a MySQL table."""
    try:
        cursor.execute(f"ALTER TABLE {table} {query}")
    except Error as e:
        error_mysql(e, f"Failed to alter table {table}.")
    else:
        sucess_mysql(f"Table {table} altered successfully.")
