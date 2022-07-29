import sqlite3
import psycopg2
import os
from pathlib import Path
from db.db import connect


if __name__ == '__main__':
    con, cursor = connect()
    for file in ['delete.sql', 'create.sql']:
        for query in open(Path('db').joinpath('SQL').joinpath(file)).read().strip().split(';'):
            print(query)
            if query.strip() != '':
                cursor.execute(query)

        con.commit()
