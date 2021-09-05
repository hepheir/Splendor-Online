from collections import defaultdict
from enum import IntEnum, auto
from random import shuffle

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


class Game:
    def __init__(self, host_user: User) -> None:
        """Constructor

        Args:
            host_user: (User) 방장의 User 모델
        """
        assert isinstance(host_user, User)
        print(f'[SYSTEM] Player {host_user} wants to create a game.')
        self._game_id: int = host_user.db_row["user_id"]
        database.insert_one('game', value={"game_id": self.game_id,
                                           "game_state": GAME_STATE.PRE_GAME})
        database.update_one('user',
                            query={"user_id": host_user.db_row["user_id"]},
                            value={"game_id": self.game_id})
        print(f'[SYSTEM] Player {host_user} successfully created {self}.')
        print()

    def __repr__(self) -> str:
        return f'<game_id:{self.game_id}>'

    def __del__(self) -> None:
        """Destructor"""
        for user_db_row in self.player_db_rows:
            database.update_one('user',
                                query={"user_id": user_db_row["user_id"]},
                                value={"game_id": None})
        database.delete_all('game_component', query={"game_id": self.game_id})
        database.delete_all('game', query={"game_id": self.game_id})
        print(f'[SYSTEM] Game {self} has expired.')
        print()

    @property
    def game_id(self):
        return self._game_id

    @property
    def db_row(self):
        return database.select_one('game', {"game_id": self.game_id})

    @property
    def n_players(self) -> int:
        return len(self.player_db_rows)

    @property
    def player_db_rows(self):
        return database.select_all('user', query={"game_id": self.game_id})

    @property
    def game_state(self):
        return self.db_row["game_state"]

    @game_state.setter
    def game_state(self, new_state: GAME_STATE):
        database.update_one('game',
                            value={"game_state": new_state},
                            query={"game_id": self.game_id})

    @property
    def coins_to_discard(self):
        if self.n_players == 2:
            return 3
        elif self.n_players == 3:
            return 2
        else:
            return 0
