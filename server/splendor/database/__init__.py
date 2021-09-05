import glob
import os
import sqlite3
import typing as t


FILE_DATABASE_DB = os.path.join('splendor', 'database', 'db', 'database.db')
DIR_SQL_SCRIPTS = os.path.join('splendor', 'database', 'sql')


CONNECTION: t.Optional[sqlite3.Connection] = None


def dict_factory(cursor: sqlite3.Cursor, row: t.Any):
    _dict = {}
    for index, column in enumerate(cursor.description):
        _dict[column[0]] = row[index]
    return _dict


def connect_to_db() -> sqlite3.Connection:
    """Get SQLite3 Database Connection

    Usage:
    >>> with get_database_connection() as connection:
    ...     cursor = connection.cursor()
    ...     cursor.execute("SELECT * FROM User WHERE user_name='Hepheir'")
    ...     data = tuple(cursor.fetchone())

    >>> data
    ('Hepheir', 'admin', 0, None)
    """
    global CONNECTION
    if CONNECTION is None:
        CONNECTION = sqlite3.connect(FILE_DATABASE_DB)
        CONNECTION.row_factory = dict_factory
    return CONNECTION


def connect(func):
    """Decorator to open a sqlite database connection when needed."""
    connection = connect_to_db()
    def inner_func(*args, **kwargs):
        return func(connection, *args, **kwargs)
    return inner_func


def setup_sample_data():
    print('Setting up database...')
    # 데이터 베이스 구축을 위한 SQL 스크립트 실행
    for sql_file in glob.glob(os.path.join(DIR_SQL_SCRIPTS, '*')):
        print(f'  Executing SQL script: {sql_file}')
        # 파일 속의 sql 스크립트를 읽어옴
        with open(sql_file, 'r', encoding='utf-8') as file_io:
            sql_script = file_io.read()
        # DB에 연결 후 스크립트를 실행
        with connect_to_db() as connection:
            cursor = connection.cursor()
            cursor.executescript(sql_script)


from splendor.database.crud import *


__all__ = [
    "connect",
    "connect_to_db",
    "setup_sample_data",

    "select_one",
    "select_all",
    "insert_one",
    "update_one",
    "delete_all",
]


if __name__ == "__main__":
    setup_sample_data()
