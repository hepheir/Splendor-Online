from enum import IntEnum, auto

from splendor import database


class COMPONENT_TYPE(IntEnum):
    CARD = auto()
    TILE = auto()
    COIN = auto()


class COIN_TYPE(IntEnum):
    GOLD = 0
    DIAMOND = 1
    SAPPHIRE = 2
    EMERALD = 3
    RUBY = 4
    ONYX = 5


class GAME_STATE(IntEnum):
    PRE_GAME = auto()
    START_GAME = auto()
    END_GAME = auto()
    BEGIN_ROUND = auto()
    END_ROUND = auto()
    BEGIN_TURN = auto()
    END_TURN = auto()
    WAITING_FOR_PRE_ACTION = auto()
    WAITING_FOR_POST_ACTION = auto()


class User:
    def __init__(self, name: str) -> None:
        print(f'[SYSTEM] Creating user with name "{name}"...')
        self._user_name = name
        if self.db_row:
            print(f'[ERROR] User with name: "{name}" already exists.')
            print()
            return
        database.insert_one('user', value={"user_name": self.user_name})
        print(f'[SYSTEM] Successfully created {self}.')
        print()

    def __repr__(self) -> str:
        return f'<user_name:{self.user_name}>'

    def __del__(self) -> None:
        database.delete_all('user', query={"user_name": self.user_name})
        print(f'[SYSTEM] User {self} has expired.')
        print()

    @property
    def user_name(self) -> str:
        return self._user_name

    @property
    def db_row(self):
        return database.select_one('user', query={"user_name": self.user_name})
