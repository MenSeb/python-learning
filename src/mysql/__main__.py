"""MySQL main."""


from __future__ import annotations

import sys
from logging import INFO, basicConfig, info
from os import environ as env

from database import connect_database, delete_database, use_database
from dotenv import find_dotenv, load_dotenv
from queries import EMPLOYE_QUERY, EMPLOYE_TABLE, TASK_QUERY, TASK_TABLE
from record import (
    delete_record,
    insert_record,
    insert_records,
    select_record,
    update_record,
)
from table import alter_table, create_table, delete_table, describe_table

load_dotenv(find_dotenv())

basicConfig(level=INFO)

if __name__ == "__main__":
    config = {
        "user": env.get("DATABASE_USER"),
        "password": env.get("DATABASE_PASSWORD"),
        "database": env.get("DATABASE_NAME"),
        "host": env.get("DATABASE_HOST"),
        "port": env.get("DATABASE_PORT"),
        "autocommit": True,
    }

    cnx = connect_database(**config)
    cnx.reconnect()
    cursor = cnx.cursor()

    if hasattr(cnx, "errno"):
        sys.exit(1)

    use_database(config["database"], cursor)

    describe_table("test", cursor)

    delete_table(TASK_TABLE, cursor)
    delete_table(EMPLOYE_TABLE, cursor)

    create_table(EMPLOYE_TABLE, EMPLOYE_QUERY, cursor)
    create_table(TASK_TABLE, TASK_QUERY, cursor)

    describe_table(TASK_TABLE, cursor)

    for row in cursor.fetchall():
        info(row)

    alter_table(TASK_TABLE, "title", "VARCHAR(100)", cursor)

    describe_table(TASK_TABLE, cursor)

    for row in cursor.fetchall():
        info(row)

    insert_record(
        EMPLOYE_TABLE,
        "(first_name, last_name, email, phone)",
        "('seb', 'men', 'test@gmail.com', '450-450-4500')",
        cursor,
    )

    select_record(EMPLOYE_TABLE, "email = 'test@gmail.com'", cursor)

    info(f"{cursor.fetchall()}")

    update_record(
        EMPLOYE_TABLE,
        "email = 'menseb@gmail.com'",
        "first_name = 'seb'",
        cursor,
    )

    select_record(EMPLOYE_TABLE, "email = 'menseb@gmail.com'", cursor)

    info(f"{cursor.fetchall()}")

    delete_record(EMPLOYE_TABLE, "email = 'menseb@gmail.com'", cursor)

    select_record(EMPLOYE_TABLE, "email = 'menseb@gmail.com'", cursor)

    info(f"{cursor.fetchall()}")

    insert_records(
        EMPLOYE_TABLE,
        "(first_name, last_name, email, phone)",
        "(%s, %s, %s, %s)",
        [
            ("seb", "men", "test1@gmail.com", "450-450-4500"),
            ("seb", "men", "test2@gmail.com", "450-450-4500"),
        ],
        cursor,
    )

    select_record(EMPLOYE_TABLE, "email LIKE '%test%'", cursor)

    for row in cursor.fetchall():
        info(row)

    select_record(EMPLOYE_TABLE, None, cursor)

    info(f"{cursor.fetchall()}")

    delete_record(EMPLOYE_TABLE, "email LIKE '%test%'", cursor)

    select_record(EMPLOYE_TABLE, "email LIKE '%test%'", cursor)

    info(f"{cursor.fetchall()}")

    delete_database(config["database"], cursor)

    cnx.close()