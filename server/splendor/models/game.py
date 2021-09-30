# -*- coding: utf-8 -*-

from __future__ import annotations
from enum import IntEnum, auto

import typing as t
from collections import defaultdict, Counter
from uuid import uuid4
from random import shuffle

from splendor.models.components import Card
from splendor.models.components import Tile
from splendor.models.components import CARDS_BY_LEVEL
from splendor.models.components import CARD_LEVELS
from splendor.models.components import GEM_TYPES
from splendor.models.components import TILES
from splendor.models.components import GOLD
from splendor.models.components import _T_CARD_LEVEL
from splendor.models.components import _T_GEM_TYPE


_T_UUID = str



class GAME_STATE(IntEnum):
    PRE_GAME = auto()
    SETTING_UP = auto()


class PLAYER_STATE(IntEnum):
    WAITING = auto()
    PLAYING = auto()


class Player(object):
    def __init__(self, game: Game, name: str) -> None:
        self.uuid: _T_UUID
        self.game: Game
        self.state: PLAYER_STATE
        self.name: str
        self.points: int
        self.cards: t.DefaultDict[_T_GEM_TYPE, t.List[Card]]
        self.reserved: t.List[Card]
        self.tokens: t.Counter[_T_GEM_TYPE]
        self.tiles: t.List[Tile]

        self.uuid = str(uuid4())
        self.game = game
        self.name = ""
        self.state = PLAYER_STATE.WAITING
        self.tokens = Counter()
        self.cards = defaultdict(list)
        self.reserved = []
        self.tiles = []
        self.points = 0

    def as_dict(self) -> t.Dict[str, t.Any]:
        return {
            "uuid": self.uuid,
            "name": self.name,
            "points": self.points,
            "tiles": self.tiles,
            "reserved": self.reserved,
            "cards": {
                gem_type: [card.as_dict() for card in self.cards[gem_type]]
                for gem_type in GEM_TYPES
            },
            "tokens": {
                gem_type: self.tokens[gem_type] for gem_type in GEM_TYPES
            },
        }


class Game:
    def __init__(self) -> None:
        self.uuid: _T_UUID
        self.state: GAME_STATE
        self.players: t.List[Player]
        self.cards: t.Dict[_T_CARD_LEVEL, t.List[Card]]
        self.card_drawpiles: t.Dict[_T_CARD_LEVEL, t.List[Card]]
        self.tiles: t.List[Tile]
        self.tokens: t.Counter[_T_GEM_TYPE]
        self.log: t.List[str]
        self.is_last_round: bool
        self.current_player_index: int

        self.uuid = str(uuid4())
        self.state = GAME_STATE.PRE_GAME
        self.players = []

        GAMES[self.uuid] = self

    def start_game(self) -> None:
        assert self.state is GAME_STATE.PRE_GAME
        self.state = GAME_STATE.SETTING_UP
        # Default Settings
        n_players = len(self.players)
        n_coins = 7
        n_cards = 4
        n_tiles = n_players + 1
        # Setting up Tokens
        if n_players == 3:
            n_coins -= 2
        elif n_players == 2:
            n_coins -= 3
        self.tokens = Counter()
        for gem_type in GEM_TYPES:
            self.tokens[gem_type] += n_coins
        self.tokens[GOLD] = 5
        # Setting up Cards
        self.card_drawpiles = {lv: [] for lv in CARD_LEVELS}
        self.cards = {lv: [] for lv in CARD_LEVELS}
        for lv in CARD_LEVELS:
            self.card_drawpiles[lv] = CARDS_BY_LEVEL[lv].copy()
            shuffle(self.card_drawpiles[lv])
            for i in range(n_cards):
                card = self.card_drawpiles[lv].pop()
                self.cards[lv].append(card)
        # Setting up Tiles
        _tiles = list(TILES.values())
        shuffle(_tiles)
        self.tiles = _tiles[:n_tiles]
        # Setting up Flags
        self.is_last_round = False
        self.current_player_index = 0
        self.log = []

    def current_player(self) -> Player:
        return self.players[self.current_player_index]

    def begin_turn(self) -> None:
        player = self.current_player()
        player.state = PLAYER_STATE.PLAYING

    def end_turn(self) -> None:

        pass

    def take(self, tokens: t.Counter[_T_GEM_TYPE]) -> None:
        player = self.current_player()
        for gem_type in GEM_TYPES:
            self.tokens[gem_type] -= tokens[gem_type]
            player.tokens[gem_type] += tokens[gem_type]

    def as_dict(self) -> dict:
        return {
            "uuid": self.uuid,
            "players": [player.uuid for player in self.players],
            "cards": {
                level: [card.uuid for card in self.cards[level]]
                for level in CARD_LEVELS
            },
            "card_drawpiles": {
                level: len(self.card_drawpiles[level]) for level in CARD_LEVELS
            },
            "tiles": [tile.uuid for tile in self.tiles],
            "tokens": {
                gem_type: self.tokens[gem_type] for gem_type in GEM_TYPES
            },
            "is_last_round": self.is_last_round,
            "current_player_index": self.current_player_index,
        }

    def on_message(self, player_id: int, message: str) -> None:
        pass

    def on_end_turn(self) -> None:
        pass


game = Game()
game.start_game()
