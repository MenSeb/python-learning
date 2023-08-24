"""Modules to handle a MySQL database."""

from __future__ import annotations

import sys
from logging import info

from error import error_mysql

import mysql.connector as mysqlc
from mysql.connector import cursor, errorcode


def connect_database(**options: str) -> mysqlc.MySQLConnection:
    """Connect to a MySQL database."""
    try:
        return mysqlc.connect(**options)
    except (AttributeError, mysqlc.Error) as e:
        if hasattr(e, "errno") and e.errno == errorcode.ER_BAD_DB_ERROR:
            database = options.pop("database")
            cnx = mysqlc.connect(**options)
            create_database(database, cnx.cursor())
            cnx.database = database
            return cnx
        error_mysql(e, "Failed to connect to mysql database.")
        sys.exit(1)


def delete_database(database: str, cursor: cursor.MySQLCursor) -> None:
    """Delete a MySQL database."""
    try:
        cursor.execute(f"DROP DATABASE {database}")
        info(f"Database {database} deleted successfully.")
    except mysqlc.Error as e:
        error_mysql(e, f"Failed to delete database {database}")


def create_database(database: str, cursor: cursor.MySQLCursor) -> None:
    """Create a MySQL database."""
    try:
        cursor.execute(f"CREATE DATABASE {database}")
        info(f"Database {database} created successfully.")
    except mysqlc.Error as e:
        error_mysql(e, f"Failed to create database {database}.")


def use_database(database: str, cursor: cursor.MySQLCursor) -> None:
    """Use a MySQL database."""
    try:
        cursor.execute(f"USE {database}")
        info(f"Database {database} used successfully.")
    except mysqlc.Error as e:
        error_mysql(e, f"Failed to use database {database}.")
