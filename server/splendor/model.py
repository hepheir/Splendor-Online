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
        self._user_name = name

        if self.db_row:
            print(f"User with name: [{self.user_name}] already exists.")
            return
        else:
            database.insert_one('user', value={"user_name": self.user_name})

    def __del__(self) -> None:
        database.delete_all('user', query={"user_name": self.user_name})

    @property
    def user_name(self) -> str:
        return self._user_name

    @property
    def db_row(self):
        return database.select_one('user', query={"user_name": self.user_name})


class Game:
    def __init__(self, host_id: int) -> None:
        """Constructor

        Args:
            host_id: (int) 방장의 user_id
        """
        self._game_id: int = host_id

        database.insert_one('game', value={"game_id": self.game_id})
        self.join(host_id)

    def __del__(self) -> None:
        """Destructor"""
        for user in self.players:
            database.update_one('user',
                                query={"user_id": user["user_id"]},
                                value={"game_id": None})
        database.delete_all('game_component', query={"game_id": self.game_id})
        database.delete_all('game', query={"game_id": self.game_id})

    @property
    def game_id(self):
        return self._game_id

    @property
    def db_row(self):
        return database.select_one('game', {"game_id": self.game_id})

    @property
    def game_state(self):
        return self.db_row["game_state"]

    @game_state.setter
    def game_state(self, new_state: GAME_STATE):
        database.update_one('game',
                            value={"game_state": new_state},
                            query={"game_id": self.game_id})

    @property
    def players(self):
        return database.select_all('user',
                                   query={"game_id": self.game_id})

    @property
    def coins_to_discard(self):
        if len(self.players) == 2:
            return 3
        elif len(self.players) == 3:
            return 2
        else:
            return 0

    def join(self, user_id: int) -> None:
        if self.game_state is not None:
            print('Unable to join the game.')
            return
        database.update_one('user',
                            query={"user_id": user_id},
                            value={"game_id": self.game_id})

    def setup_game(self) -> None:
        tiles = database.select_all('tile')[:len(self.players)+1]
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
