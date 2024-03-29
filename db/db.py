import sqlite3
import psycopg2
from dotenv import load_dotenv
import pathlib
import os

load_dotenv(str(pathlib.Path(__file__).parent.parent.joinpath('.env')))


def connect_sqlite3():
    conn = sqlite3.connect('db/data.db')
    cursor = conn.cursor()
    return conn, cursor


def connect_postgres_local():
    conn = psycopg2.connect(
        database='pizza_bot_db',
        user='pizza_user',
        password='pizza'
    )
    return conn, conn.cursor()


def connect_postgres():
    conn = psycopg2.connect(
        database='d2vqfbhdetfr8m',
        user='gtlhzircpzzgnq',
        password=os.environ['DB_PASSWORD'],
        host='ec2-54-170-90-26.eu-west-1.compute.amazonaws.com',
        port=5432
    )
    return conn, conn.cursor()


def connect(db_v='postgres', db=os.environ['DB']):
    if db_v == 'postgres':
        if db == 'local':
            return connect_postgres_local()
        elif db == 'heroku':
            return connect_postgres()
    elif db == 'sqlite3':
        return connect_sqlite3()
