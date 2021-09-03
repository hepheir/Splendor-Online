import glob
import os
import sqlite3


FILE_DATABASE_DB = os.path.join('splendor', 'database', 'db', 'database.db')
DIR_SQL_SCRIPTS = os.path.join('splendor', 'database', 'sql')


def setup_sample_data():
    print('Setting up database...')

    # 데이터 베이스 구축을 위한 SQL 스크립트 실행
    for sql_file in glob.glob(os.path.join(DIR_SQL_SCRIPTS, '*')):
        print(f'  Executing SQL script: {sql_file}')

        with open(sql_file, 'r', encoding='utf-8') as file_io:
            sql_script = file_io.read()

        with get_database_connection() as connection:
            cursor = connection.cursor()
            cursor.executescript(sql_script)


def get_database_connection() -> sqlite3.Connection:
    """Get SQLite3 Database Connection

    Usage:
    >>> with get_database_connection() as connection:
    ...     cursor = connection.cursor()
    ...     cursor.execute("SELECT * FROM User WHERE user_name='Hepheir'")
    ...     data = tuple(cursor.fetchone())

    >>> data
    ('Hepheir', 'admin', 0, None)
    """
    return sqlite3.connect(FILE_DATABASE_DB)


if __name__ == "__main__":
    setup_sample_data()
