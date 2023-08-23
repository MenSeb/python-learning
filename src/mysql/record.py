"""Modules to handle a MySQL record."""

from __future__ import annotations

from logging import error, info

from mysql.connector import Error, cursor


def insert_record(
    table: str,
    attrs: list[str],
    vals: list[str],
    cursor: cursor.MySQLCursor,
) -> None:
    """Insert a record in a MySQL table."""
    try:
        cursor.execute(f"INSERT INTO {table} {attrs} VALUES {vals}")
        info(f"Data in table {table} inserted successfully.")
    except Error as e:
        error(f"Failed to insert data in table {table}.")
        error(e)


def insert_records(
    table: str,
    attrs: str,
    vals: str,
    records: list[tuple],
    cursor: cursor.MySQLCursor,
) -> None:
    """Insert multiple records in a MySQL table."""
    try:
        cursor.executemany(f"INSERT INTO {table} {attrs} VALUES {vals}", records)
        info(f"Data in table {table} inserted successfully.")
    except Error as e:
        error(f"Failed to insert data in table {table}.")
        error(e)


def select_record(
    table: str,
    condition: str | None,
    cursor: cursor.MySQLCursor,
) -> None:
    """Read a record in a MySQL table."""
    try:
        query = f"SELECT * FROM {table}"
        if condition:
            query += f" WHERE {condition}"
        cursor.execute(query)
        info(f"Data in table {table} selected successfully.")
    except Error as e:
        error(f"Failed to select data in table {table}.")
        error(e)


def update_record(
    table: str,
    assignment: str,
    condition: str,
    cursor: cursor.MySQLCursor,
) -> None:
    """Update a record in a MySQL table."""
    try:
        cursor.execute(f"UPDATE {table} SET {assignment} WHERE {condition}")
        info(f"Data in table {table} updated successfully.")
    except Error as e:
        error(f"Failed to update data in table {table}.")
        error(e)


def delete_record(table: str, condition: str, cursor: cursor.MySQLCursor) -> None:
    """Delete a record in a MySQL table."""
    try:
        cursor.execute(f"DELETE FROM {table} WHERE {condition}")
        info(f"Data in table {table} deleted successfully.")
    except Error as e:
        error(f"Failed to delete data in table {table}.")
        error(e)
