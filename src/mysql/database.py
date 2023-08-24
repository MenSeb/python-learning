"""Modules to handle a MySQL database."""

from __future__ import annotations

from logging import error, info

from mysql.connector import Error, MySQLConnection, connect, cursor, errorcode


def connect_database(
    database: str,
    *,
    autocommit: bool,
    **config: str,
) -> MySQLConnection | Error:
    """Connect a MySQL database."""
    try:
        with connect(**config) as cnx:
            info("MySQL connected successfully.")
            cnx.autocommit = autocommit
            if database:
                create_database(database, cnx.cursor())
                cnx.database = database
                info(f"Database {database} connected successfully.")
            return cnx
    except Error as e:
        error("Failed to connect MySQL.")
        error(e)
        return e


def delete_database(name: str, cursor: cursor.MySQLCursor) -> None:
    """Delete a MySQL database."""
    try:
        cursor.execute(f"DROP DATABASE {name}")
        info(f"Database {name} deleted successfully.")
    except Error as e:
        error(f"Failed to delete database {name}")
        error(e)


def create_database(name: str, cursor: cursor.MySQLCursor) -> None:
    """Create a MySQL database."""
    try:
        cursor.execute(f"CREATE DATABASE {name}")
        info(f"Database {name} created successfully.")
    except Error as e:
        if e.errno == errorcode.ER_DB_CREATE_EXISTS:
            info(f"Database {name} already exists.")
        else:
            error(f"Failed to create database {name}.")
            error(e)


def use_database(name: str, cursor: cursor.MySQLCursor) -> None:
    """Use a MySQL database."""
    try:
        cursor.execute(f"USE {name}")
        info(f"Database {name} used successfully.")
    except Error as e:
        error(f"Failed to use database {name}.")
        error(e)
