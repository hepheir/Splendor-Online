from collections import Counter, defaultdict
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

    @classmethod
    def int2name(cls, value: int) -> str:
        for coin_type in COIN_TYPE:
            if coin_type == value:
                return coin_type.name
        raise ValueError(f"Couldn't find the name of {value}.")

    @classmethod
    def name2int(cls, name: str) -> int:
        return getattr(cls, name.upper())


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
                                           "game_state": GAME_STATE.PRE_GAME,
                                           "game_turn": 0})
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
    def game_turn(self):
        return self.db_row["game_turn"]

    @game_turn.setter
    def game_turn(self, value: int):
        database.update_one('game',
                            value={"game_turn": value},
                            query={"game_id": self.game_id})

    @property
    def current_player_db_row(self):
        return self.player_db_rows[(self.game_turn-1) % self.n_players]

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
        self.game_turn = 0
        print(f'[SYSTEM] Finish setting up the {self}.')
        print()

    def start_game(self):
        print(f'[SYSTEM] Preparing for starting the game {self}...')
        if self.game_state != GAME_STATE.PRE_GAME:
            print(f'[ERROR] The game has already been started.')
            print(f'[ERROR] * State of the game is {self.game_state}.')
            print()
            return
        elif self.n_players < 2:
            print(f'[ERROR] Not enough players to start the game.')
            print(f'[ERROR] * There are {self.n_players} player(s).')
            print()
            return
        else:
            self.game_state = GAME_STATE.START_GAME
            self.setup_game()
            print(f'[SYSTEM] Start the game {self}.')
            print()
            self.begin_round()

    def begin_round(self):
        print(f'[SYSTEM] Preparing for begining the round...')
        if self.game_state not in [GAME_STATE.START_GAME, GAME_STATE.END_ROUND]:
            print(f'[ERROR] Unable to begin the round.')
            print(f'[ERROR] * You are accessing from wrong state'
                  f' <game_state:{self.game_state}>.')
            print()
            return
        self.game_state = GAME_STATE.BEGIN_ROUND
        _round_no = self.game_turn // self.n_players + 1
        print(f'[SYSTEM] Beginning the round #{_round_no}.')
        print()
        self.begin_turn()

    def begin_turn(self):
        print(f'[SYSTEM] Preparing for begining the turn...')
        if self.game_state not in [GAME_STATE.BEGIN_ROUND, GAME_STATE.END_TURN]:
            print(f'[ERROR] Unable to begin the round.')
            print(f'[ERROR] * You are accessing from wrong state'
                  f' <game_state:{self.game_state}>.')
            print()
            return
        self.game_state = GAME_STATE.BEGIN_TURN
        self.game_turn += 1
        _user_db_row = self.current_player_db_row
        print(f'[SYSTEM] Beginning the turn #{self.game_turn}.')
        print(f"[SYSTEM] {_user_db_row['user_name']}'s Turn")
        print()

    def action(self, user: User, action_type: str, **data):
        print(f'[SYSTEM] Preparing for <action_type:{action_type}>...')
        print(f'[SYSTEM] * Action was requested from: {user}')
        if self.game_state != GAME_STATE.BEGIN_TURN:
            print(f'[ERROR] Unable to do the action.')
            print(f'[ERROR] * You are accessing from wrong state'
                  f' <game_state:{self.game_state}>.')
            print()
            return
        elif user.db_row['user_id'] != self.current_player_db_row['user_id']:
            print(f'[ERROR] Unable to do the action.')
            print(f"[ERROR] * This is not {user}'s turn.")
            print()
            return
        if action_type == 'gain_coin':
            self._action_gain_coin(user, **data)
        elif action_type == 'buy_card':
            # TODO
            raise NotImplementedError()
        elif action_type == 'reserve_card':
            # TODO
            raise NotImplementedError()
        else:
            print(f'[ERROR] Unable to do the action.')
            print(f"[ERROR] <action_type:{action_type}> is not a valid"
                  f" type of action.")
            print()
            return

    def _action_gain_coin(self, user: User, **data):
        print(f'[SYSTEM] Checking for prerequisites...')
        coins_reserved = Counter()
        coins_requested = Counter()
        # Check coins that already have been taken
        connection = database.connect_to_db()
        coin_db_rows = connection.execute("""
            SELECT
                game_id,
                component_id,
                component_type,
                src_id,
                dst_id,
                coin_type
            FROM
                game_transaction
                LEFT JOIN
                    coin
            WHERE
                game_id=? -- game.game_id
                AND
                component_type=? -- component_type.coin
                AND
                component_id=coin_id
                AND
                src_id is NULL
                AND
                dst_id is ? -- user.user_id
        """, (self.game_id, COMPONENT_TYPE.COIN, user.db_row['user_id']))
        for coin_db_row in coin_db_rows:
            coins_reserved[coin_db_row['coin_type']] += 1
        for key, value in data.items():
            coin_type = COIN_TYPE.name2int(key)
            coins_requested[coin_type] = value
        # Analyse data
        coins_to_reserve = coins_reserved + coins_requested
        n_diff_coin_types = len(coins_to_reserve)
        n_total_coins = sum(coins_to_reserve.values())
        # Console logging
        if sum(coins_reserved.values()) == 0:
            print(f'[SYSTEM] * {user} has not gained any coin yet.')
        else:
            print(f'[SYSTEM] * {user} has taken')
            for coin_type, amount in coins_reserved.items():
                coin_name = COIN_TYPE.int2name(coin_type)
                print(f'[SYSTEM]   * {coin_name} x{amount}')
        print(f'[SYSTEM] * {user} requested following coins:')
        for coin_type, amount in coins_requested.items():
            coin_name = COIN_TYPE.int2name(coin_type)
            print(f'[SYSTEM]   * {coin_name} x{amount}')
        # Checking if the request is valid
        if sum(coins_to_reserve.values()) > 3:
            # Case of taking more than 3 coins a turn.
            print(f'[ERROR] You can only gain coins less than 4 a turn.')
            print(f"[ERROR] You've tried to gain {n_total_coins} coins.")
            print()
            return
        elif len(coins_to_reserve) > 1 and coins_to_reserve.most_common(1)[0][1] > 2:
            # Case of taking 2 or more diffrent types of coins,
            # while taking 2 or more coins from same type.
            print(f'[ERROR] You can either take 3 (or less) coins of'
                  f' diffrent types, or take only 2 coins of same type.')
            print()
            return
        print(f'[SYSTEM] Reserving coins...')
        for coin_type, amount in coins_requested.items():
            connection = database.connect_to_db()
            connection.execute("""
                INSERT INTO
                    game_transaction
                SELECT
                    game_id,
                    component_id,
                    component_type,
                    owner_id as src_id,
                    1 as dst_id
                FROM
                    game_component
                    LEFT JOIN
                        coin
                WHERE
                    game_id=? -- game.game_id
                    AND
                    component_type=? -- component_type.coin
                    AND
                    coin_type=? -- coin_type
                    AND
                    component_id=coin_id
                    AND
                    owner_id is NULL
                LIMIT
                    ? -- amount
            """, (self.game_id, COMPONENT_TYPE.COIN, coin_type, amount))
        print(f'[SYSTEM] Reserved coins.')
        print(f'[SYSTEM] Checking for end of a action.')
        # TODO: Gold is unobtainable
        # TODO: Should end the turn
        # TODO: Should return the coin
