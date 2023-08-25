"""Modules to handle a MySQL database."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from logger import error_mysql, sucess_mysql

from mysql.connector import Error, MySQLConnection, connect, errorcode

if TYPE_CHECKING:
    from mysql.connector.cursor import MySQLCursor


def connect_database(**options: str) -> MySQLConnection:
    """Connect to a MySQL database."""
    try:
        cnx = connect(**options)
        database = options.get("database")
        database = "" if not database else f" {database}"
    except (AttributeError, Error) as e:
        if hasattr(e, "errno") and e.errno == errorcode.ER_BAD_DB_ERROR:
            database = options.pop("database")
            cnx = connect(**options)
            create_database(database, cnx.cursor())
            cnx.database = database
            sucess_mysql(f"Database {database} connected successfully")
            return cnx
        error_mysql(e, "Failed to connect to mysql database.")
        sys.exit(1)
    else:
        sucess_mysql(f"Database{database} connected successfully")
        return cnx


def delete_database(database: str, cursor: MySQLCursor) -> None:
    """Delete a MySQL database."""
    try:
        cursor.execute(f"DROP DATABASE {database}")
    except Error as e:
        error_mysql(e, f"Failed to delete database {database}")
    else:
        sucess_mysql(f"Database {database} deleted successfully.")


def create_database(database: str, cursor: MySQLCursor) -> None:
    """Create a MySQL database."""
    try:
        cursor.execute(f"CREATE DATABASE {database}")
    except Error as e:
        error_mysql(e, f"Failed to create database {database}.")
    else:
        sucess_mysql(f"Database {database} created successfully.")


def use_database(database: str, cursor: MySQLCursor) -> None:
    """Use a MySQL database."""
    try:
        cursor.execute(f"USE {database}")
    except Error as e:
        error_mysql(e, f"Failed to use database {database}.")
    else:
        sucess_mysql(f"Database {database} used successfully.")
