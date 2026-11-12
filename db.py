"""Работа с базой данных PostgreSQL через библиотеку psycopg (submodule lib/postgresql)."""
import os
import sys

# подключаем библиотеку из подмодуля (пакет лежит в lib/postgresql/psycopg/psycopg)
LIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib", "postgresql", "psycopg")
sys.path.insert(0, LIB)

import psycopg  # noqa: E402
from psycopg.lab_utils import table_exists  # noqa: E402

from db_config import DSN  # noqa: E402
from parts import load_parts  # noqa: E402


def init_db(conn):
    if not table_exists(conn, "parts"):
        conn.execute(
            "CREATE TABLE parts (code VARCHAR(16) PRIMARY KEY,"
            " name TEXT NOT NULL, qty INTEGER NOT NULL)"
        )
        print("Таблица parts создана")
    else:
        print("Таблица parts уже существует")


def load_to_db(conn, path="parts.txt"):
    conn.execute("TRUNCATE parts")
    with conn.cursor() as cur:
        cur.executemany(
            "INSERT INTO parts (code, name, qty) VALUES (%(code)s, %(name)s, %(qty)s)",
            load_parts(path),
        )


def low_stock_db(conn, limit=10):
    return conn.execute(
        "SELECT code, name, qty FROM parts WHERE qty < %s ORDER BY qty", (limit,)
    ).fetchall()


if __name__ == "__main__":
    with psycopg.connect(DSN) as conn:
        print("psycopg", psycopg.__version__, "из", os.path.relpath(psycopg.__file__))
        print("реализация:", psycopg.pq.__impl__, "| сервер PostgreSQL:", conn.info.server_version)
        init_db(conn)
        load_to_db(conn)
        print("Записей в БД:", conn.execute("SELECT count(*) FROM parts").fetchone()[0])
        print("Мало на складе:", low_stock_db(conn))
