"""Modules to handMySQLCursorcursorle a MySQL record."""

from __future__ import annotations

from typing import TYPE_CHECKING

from logger import error_mysql, sucess_mysql

from mysql.connector import Error

if TYPE_CHECKING:
    from mysql.connector.cursor import MySQLCursor


def insert_record(
    table: str,
    columns: list[str],
    values: list[str],
    cursor: MySQLCursor,
) -> None:
    """Insert a record in a MySQL table."""
    try:
        cursor.execute(f"INSERT INTO {table} {columns} VALUES {values}")
    except Error as e:
        error_mysql(e, f"Failed to insert data in table {table}.")
    else:
        sucess_mysql(f"Data in table {table} inserted successfully.")


def insert_records(
    table: str,
    attrs: str,
    vals: str,
    records: list[tuple],
    cursor: MySQLCursor,
) -> None:
    """Insert multiple records in a MySQL table."""
    try:
        cursor.executemany(f"INSERT INTO {table} {attrs} VALUES {vals}", records)
    except Error as e:
        error_mysql(e, f"Failed to insert data in table {table}.")
    else:
        sucess_mysql(f"Data in table {table} inserted successfully.")


def select_record(
    table: str,
    condition: str | None,
    cursor: MySQLCursor,
) -> None:
    """Read a record in a MySQL table."""
    try:
        query = f"SELECT * FROM {table}"
        if condition:
            query += f" WHERE {condition}"
        cursor.execute(query)
    except Error as e:
        error_mysql(e, f"Failed to select data in table {table}.")
    else:
        sucess_mysql(f"Data in table {table} selected successfully.")


def update_record(
    table: str,
    assignment: str,
    condition: str,
    cursor: MySQLCursor,
) -> None:
    """Update a record in a MySQL table."""
    try:
        cursor.execute(f"UPDATE {table} SET {assignment} WHERE {condition}")
    except Error as e:
        error_mysql(e, f"Failed to update data in table {table}.")
    else:
        sucess_mysql(f"Data in table {table} updated successfully.")


def delete_record(table: str, condition: str, cursor: MySQLCursor) -> None:
    """Delete a record in a MySQL table."""
    try:
        cursor.execute(f"DELETE FROM {table} WHERE {condition}")
    except Error as e:
        error_mysql(e, f"Failed to delete data in table {table}.")
    else:
        sucess_mysql(f"Data in table {table} deleted successfully.")
