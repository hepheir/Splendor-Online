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

    def join(self, user: User) -> None:
        assert isinstance(user, User)
        print(f'[SYSTEM] Player {user} wants to join the game.')
        if self.game_state != GAME_STATE.PRE_GAME:
            print(f'[ERROR] Player {user} could not join the game.')
            print(f'[ERROR] - The game has already been started,'
                  f' or the game has expired.')
            print()
            return
        database.update_one('user',
                            query={"user_id": user.db_row["user_id"]},
                            value={"game_id": self.game_id})
        print(f'[SYSTEM] Player {user} joined the game.')
        print()

    def setup_game(self) -> None:
        print(f'[SYSTEM] Start setting up the {self}.')
        tiles = database.select_all('tile')[:self.n_players+1]
        cards = database.select_all('card')
        coins = database.select_all('coin')
        shuffle(cards)
        shuffle(tiles)
        coins_discarded = defaultdict(lambda: self.coins_to_discard)
        for tile in tiles:
            database.insert_one('game_component',
                                value={"game_id": self.game_id,
                                       "component_id": tile["tile_id"],
                                       "component_type": COMPONENT_TYPE.TILE,
                                       "owner_id": None})
        for card in cards:
            database.insert_one('game_component',
                                value={"game_id": self.game_id,
                                       "component_id": card["card_id"],
                                       "component_type": COMPONENT_TYPE.CARD,
                                       "owner_id": None})
        for coin in coins:
            if coins_discarded[coin["coin_type"]] > 0:
                coins_discarded[coin["coin_type"]] -= 1
                continue
            database.insert_one('game_component',
                                value={"game_id": self.game_id,
                                       "component_id": coin["coin_id"],
                                       "component_type": COMPONENT_TYPE.COIN,
                                       "owner_id": None})
        print(f'[SYSTEM] Finish setting up the {self}.')
        print()

    def start_game(self):
        print(f'[SYSTEM] Preparing for starting the game {self}...')
        if self.game_state != GAME_STATE.PRE_GAME:
            print(f'[ERROR] The game has already been started.')
            print(f'[ERROR] - State of the game is {self.game_state}.')
            print()
            return
        elif self.n_players < 2:
            print(f'[ERROR] Not enough players to start the game.')
            print(f'[ERROR] - There are {self.n_players} player(s).')
            print()
            return
        else:
            self.game_state = GAME_STATE.START_GAME
            self.setup_game()
            print(f'[SYSTEM] Start the game {self}.')
            print()
