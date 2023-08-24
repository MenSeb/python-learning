"""MySQL main."""


from __future__ import annotations

import sys
from getpass import getpass
from logging import INFO, basicConfig, info
from os import environ

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
        "user": environ.get("DATABASE_USER") or input("Enter user: "),
        "password": environ.get("DATABASE_PASSWORD") or getpass("Enter password: "),
        "database": environ.get("DATABASE_NAME") or input("Enter database: "),
        "host": environ.get("DATABASE_HOST") or "localhost",
        "port": environ.get("DATABASE_PORT") or "3306",
        "autocommit": True,
    }

    cnx = connect_database(**config)
    cursor = cnx.cursor()

    if hasattr(cnx, "errno"):
        sys.exit(1)

    use_database(config["database"], cursor)

    describe_table("test", cursor)

    create_table(EMPLOYE_TABLE, EMPLOYE_QUERY, cursor)
    create_table(TASK_TABLE, TASK_QUERY, cursor)

    describe_table(TASK_TABLE, cursor)

    for row in cursor.fetchall():
        info(row)

    alter_table(TASK_TABLE, "MODIFY title VARCHAR(100)", cursor)

    describe_table(TASK_TABLE, cursor)

    for row in cursor.fetchall():
        info(row)

    insert_record(
        EMPLOYE_TABLE,
        "(first_name, last_name, email, phone)",
        "('seb', 'men', 'test@gmail.com', '450-450-4500')",
        cursor,
    )

    select_record(EMPLOYE_TABLE, cursor, condition="email = 'test@gmail.com'")

    info(f"{cursor.fetchall()}")

    update_record(
        EMPLOYE_TABLE,
        "email = 'menseb@gmail.com'",
        cursor,
        condition="first_name = 'seb'",
    )

    select_record(EMPLOYE_TABLE, cursor, condition="email = 'menseb@gmail.com'")

    info(f"{cursor.fetchall()}")

    delete_record(EMPLOYE_TABLE, cursor, condition="email = 'menseb@gmail.com'")

    select_record(EMPLOYE_TABLE, cursor, condition="email = 'menseb@gmail.com'")

    info(f"{cursor.fetchall()}")

    insert_records(
        EMPLOYE_TABLE,
        "(first_name, last_name, email, phone)",
        "(%s, %s, %s, %s)",
        [
            ("seb", "men", "test1@gmail.com", "450-450-4500"),
            ("seb", "men", "test2@gmail.com", "450-450-4600"),
            ("test", "men", "test3@gmail.com", "450-450-4400"),
        ],
        cursor,
    )

    select_record(EMPLOYE_TABLE, cursor, condition="first_name LIKE 'seb%'")

    for row in cursor.fetchall():
        info(row)

    select_record(EMPLOYE_TABLE, cursor)

    for row in cursor.fetchall():
        info(row)

    delete_record(
        EMPLOYE_TABLE,
        cursor,
        condition="email LIKE '%test%'",
        limit=2,
        order="phone",
    )

    select_record(EMPLOYE_TABLE, cursor, condition="email LIKE '%test%'")

    info(f"{cursor.fetchall()}")

    delete_table(TASK_TABLE, cursor)
    delete_table(EMPLOYE_TABLE, cursor)

    delete_database(config["database"], cursor)

    cnx.close()
