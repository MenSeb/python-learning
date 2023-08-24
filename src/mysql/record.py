"""Modules to handMySQLCursorcursorle a MySQL record."""

from __future__ import annotations

from typing import TYPE_CHECKING

from logger import error_mysql, sucess_mysql
from query import (
    query_columns,
    query_condition,
    query_ignore,
    query_limit,
    query_order,
    query_priority,
)

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
    columns: str,
    values: str,
    records: list[tuple],
    cursor: MySQLCursor,
) -> None:
    """Insert multiple records in a MySQL table."""
    try:
        cursor.executemany(f"INSERT INTO {table} {columns} VALUES {values}", records)
    except Error as e:
        error_mysql(e, f"Failed to insert data in table {table}.")
    else:
        sucess_mysql(f"Data in table {table} inserted successfully.")


def select_record(
    table: str,
    cursor: MySQLCursor,
    **options: bool | str | None,
) -> None:
    """Read a record in a MySQL table."""
    try:
        columns = query_columns(options.get("columns"))
        condition = query_condition(options.get("condition"))
        order = query_order(options.get("order"))
        query = f"""
            SELECT {columns}
            FROM {table}
            {condition}
            {order}
        """.rstrip()
        cursor.execute(query)
        sucess_mysql(f"{query}\n")
    except Error as e:
        error_mysql(e, f"Failed to select data in table {table}.")
    else:
        sucess_mysql(f"Data in table {table} selected successfully.")


def update_record(
    table: str,
    assignment: str,
    cursor: MySQLCursor,
    **options: bool | str | None,
) -> None:
    """Update a record in a MySQL table."""
    try:
        priority = query_priority(options.get("priority"))
        ignore = query_ignore(options.get("ignore"))
        condition = query_condition(options.get("condition"))
        query = f"""
            UPDATE {priority} {ignore} {table}
            SET {assignment}
            {condition}
        """.rstrip()
        cursor.execute(query)
        sucess_mysql(f"{query}\n")
    except Error as e:
        error_mysql(e, f"Failed to update data in table {table}.")
    else:
        sucess_mysql(f"Data in table {table} updated successfully.")


def delete_record(
    table: str,
    cursor: MySQLCursor,
    **options: bool | str | None,
) -> None:
    """Delete a record in a MySQL table."""
    try:
        condition = query_condition(options.get("condition"))
        limit = query_limit(options.get("limit"))
        order = query_order(options.get("order"))
        query = f"""
            DELETE FROM {table}
            {condition}
            {order}
            {limit}
        """.rstrip()
        cursor.execute(query)
        sucess_mysql(f"{query}\n")
    except Error as e:
        error_mysql(e, f"Failed to delete data in table {table}.")
    else:
        sucess_mysql(f"Data in table {table} deleted successfully.")
