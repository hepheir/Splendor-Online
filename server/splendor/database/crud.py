import sqlite3
from typing import Any, Dict, List

from splendor.database import connect_to_db


CONNECTION = connect_to_db()


def execute(sql: str, *params):
    cursor = CONNECTION.execute(sql, tuple(params))
    return cursor.fetchall()


def select_one(table_name: str, query: Dict[str, Any] = {}):
    sql = f"""
        SELECT
            *
        FROM
            {table_name}
    """
    if query:
        sql += f"""
        WHERE
            {' AND '.join([f'{column}=?' for column in query])}
        """
    params = tuple(query.values())
    cursor = CONNECTION.execute(sql, params)
    return cursor.fetchone()


def select_all(table_name: str, query: Dict[str, Any] = {}):
    sql = f"""
        SELECT
            *
        FROM
            {table_name}
    """
    if query:
        sql += f"""
        WHERE
            {' AND '.join([f'{column}=?' for column in query])}
        """
    params = tuple(query.values())
    cursor = CONNECTION.execute(sql, params)
    return cursor.fetchall()


def insert_one(table_name: str, value: Dict[str, Any]):
    try:
        sql = f"""
            INSERT INTO
                {table_name}({",".join([f"'{column}'" for column in value])})
            VALUES
                ({",".join(["?"]*len(value))})
        """
        params = tuple(value.values())
        CONNECTION.execute(sql, params)
        CONNECTION.commit()
    except sqlite3.IntegrityError as integrity_error:
        print(integrity_error)


def update_one(table_name: str, value: Dict[str, Any], query: Dict[str, Any] = {}):
    sql = f"""
        UPDATE
            {table_name}
        SET
            {",".join([f"{column}=?" for column in value])}
        WHERE
            {' AND '.join([f'{column}=?' for column in query])}
    """
    params = tuple(value.values())+tuple(query.values())
    CONNECTION.execute(sql, params)
    CONNECTION.commit()


def delete_all(table_name: str, query: Dict[str, Any] = {}):
    sql = f"""
        DELETE FROM
            {table_name}
        WHERE
            {' AND '.join([f'{column}=?' for column in query])}
    """
    params = tuple(query.values())
    CONNECTION.execute(sql, params)
    CONNECTION.commit()


__all__ = [
    "execute",
    "select_one",
    "select_all",
    "insert_one",
    "update_one",
    "delete_all",
]
