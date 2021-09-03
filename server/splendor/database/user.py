from dataclasses import dataclass

from splendor.database import get_database_connection


@dataclass
class User:
    user_id: int
    user_name: str
    user_password: str
    user_is_online: int
    game_id: int


def get_user_by_id(user_id: int, hide_password: bool = True) -> User:
    with get_database_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
            SELECT
                user_id,
                user_name,
                user_password,
                user_is_online,
                game_id
            FROM
                User
            WHERE
                user_id=?
        """, (user_id,))
        query_row = cursor.fetchone()
    if not query_row:
        print(f'Could not find user with id: "{user_id}"')
        return None
    else:
        user = User(*query_row)
        if hide_password:
            user.user_password = None
        return user


def get_user_by_name(user_name: str, hide_password: bool = True) -> User:
    with get_database_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
            SELECT
                user_id,
                user_name,
                user_password,
                user_is_online,
                game_id
            FROM
                User
            WHERE
                user_name=?
        """, (user_name,))
        query_row = cursor.fetchone()
    if not query_row:
        print(f'Could not find user with name: "{user_name}"')
        return None
    else:
        user = User(*query_row)
        if hide_password:
            user.user_password = None
        return user
