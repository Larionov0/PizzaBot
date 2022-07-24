import sqlite3
import psycopg2


def connect_sqlite3():
    conn = sqlite3.connect('db/data.db')
    cursor = conn.cursor()
    return conn, cursor


def connect_postgres():
    conn = psycopg2.connect(
        database='pizza_bot_db',
        user='pizza_user',
        password='pizza'
    )
    return conn, conn.cursor()


def connect(db='postgres'):
    if db == 'postgres':
        return connect_postgres()
    elif db == 'sqlite3':
        return connect_sqlite3()
