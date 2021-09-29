# -*- coding: utf-8 -*-

from __future__ import annotations

import typing as t
from random import shuffle

from splendor.models.containers import TokenContainer
from splendor.models.components import Card
from splendor.models.components import Tile
from splendor.models.components import Token
from splendor.models.enums import GEM_TYPE


class Board:
    def __init__(self) -> None:
        self.cards_1_revealed: t.List[Card] = []
        self.cards_2_revealed: t.List[Card] = []
        self.cards_3_revealed: t.List[Card] = []

        self.cards_1_drawpile: t.List[Card] = [None, None, None, None]
        self.cards_2_drawpile: t.List[Card] = [None, None, None, None]
        self.cards_3_drawpile: t.List[Card] = [None, None, None, None]

        self.tiles: t.List[Tile] = [None, None, None, None, None]
        self.tokens: TokenContainer = TokenContainer()

    def as_dict(self) -> t.Dict:
        return {
            "cards": {
                1: {
                    "revealed": self.cards_1_revealed,
                    "drawpile": len(self.cards_1_drawpile),
                },
                2: {
                    "revealed": self.cards_2_revealed,
                    "drawpile": len(self.cards_2_drawpile),
                },
                3: {
                    "revealed": self.cards_3_revealed,
                    "drawpile": len(self.cards_3_drawpile),
                },
            },
            "tiles": self.tiles,
            "tokens": self.tokens.as_dict(),
        }

    def setup(self, n_players: int) -> None:
        # Setup tiles
        shuffle(TILES)
        self.tiles = TILES[: n_players + 1]
        # Setup cards
        shuffle(CARDS_1)
        shuffle(CARDS_2)
        shuffle(CARDS_3)
        self.cards_1_revealed = CARDS_1[:4]
        self.cards_2_revealed = CARDS_2[:4]
        self.cards_3_revealed = CARDS_3[:4]
        self.cards_1_drawpile = CARDS_1[4:]
        self.cards_2_drawpile = CARDS_2[4:]
        self.cards_3_drawpile = CARDS_3[4:]
        # Setup tokens
        for token in TOKENS:
            self.tokens.insert(token)
        if n_players == 3:
            disposal = 2
        elif n_players == 2:
            disposal = 3
        else:
            disposal = 0
        for gem_type in GEM_TYPE:
            if gem_type is GEM_TYPE.GOLD:
                continue
            for _ in range(disposal):
                self.tokens.pop(gem_type)


CARDS_1 = [
    Card(1, 1, GEM_TYPE.ONYX, "onyx.mine", 0, 4, 0, 0, 0),
    Card(1, 0, GEM_TYPE.ONYX, "onyx.mine", 0, 0, 1, 3, 1),
    Card(1, 0, GEM_TYPE.ONYX, "onyx.mine", 1, 1, 1, 1, 0),
    Card(1, 0, GEM_TYPE.ONYX, "onyx.mine", 1, 2, 1, 1, 0),
    Card(1, 0, GEM_TYPE.ONYX, "onyx.mine", 0, 0, 2, 1, 0),
    Card(1, 0, GEM_TYPE.ONYX, "onyx.mine", 2, 2, 0, 1, 0),
    Card(1, 0, GEM_TYPE.ONYX, "onyx.mine", 2, 0, 2, 0, 0),
    Card(1, 0, GEM_TYPE.ONYX, "onyx.mine", 0, 0, 3, 0, 0),
    Card(1, 1, GEM_TYPE.SAPPHIRE, "sapphire.mine", 0, 0, 0, 4, 0),
    Card(1, 0, GEM_TYPE.SAPPHIRE, "sapphire.mine", 1, 0, 1, 1, 1),
    Card(1, 0, GEM_TYPE.SAPPHIRE, "sapphire.mine", 1, 0, 1, 2, 1),
    Card(1, 0, GEM_TYPE.SAPPHIRE, "sapphire.mine", 0, 0, 2, 0, 2),
    Card(1, 0, GEM_TYPE.SAPPHIRE, "sapphire.mine", 1, 0, 0, 0, 2),
    Card(1, 0, GEM_TYPE.SAPPHIRE, "sapphire.mine", 0, 0, 0, 0, 3),
    Card(1, 0, GEM_TYPE.SAPPHIRE, "sapphire.mine", 0, 1, 3, 1, 0),
    Card(1, 0, GEM_TYPE.SAPPHIRE, "sapphire.mine", 1, 0, 2, 2, 0),
    Card(1, 1, GEM_TYPE.EMERALD, "emerald.mine", 0, 0, 0, 0, 4),
    Card(1, 0, GEM_TYPE.EMERALD, "emerald.mine", 2, 1, 0, 0, 0),
    Card(1, 0, GEM_TYPE.EMERALD, "emerald.mine", 1, 3, 1, 0, 0),
    Card(1, 0, GEM_TYPE.EMERALD, "emerald.mine", 0, 2, 0, 2, 0),
    Card(1, 0, GEM_TYPE.EMERALD, "emerald.mine", 0, 0, 0, 3, 0),
    Card(1, 0, GEM_TYPE.EMERALD, "emerald.mine", 1, 1, 0, 1, 1),
    Card(1, 0, GEM_TYPE.EMERALD, "emerald.mine", 1, 1, 0, 1, 2),
    Card(1, 0, GEM_TYPE.EMERALD, "emerald.mine", 0, 1, 0, 2, 2),
    Card(1, 1, GEM_TYPE.RUBY, "ruby.mine", 4, 0, 0, 0, 0),
    Card(1, 0, GEM_TYPE.RUBY, "ruby.mine", 3, 0, 0, 0, 0),
    Card(1, 0, GEM_TYPE.RUBY, "ruby.mine", 0, 2, 1, 0, 0),
    Card(1, 0, GEM_TYPE.RUBY, "ruby.mine", 2, 0, 0, 2, 0),
    Card(1, 0, GEM_TYPE.RUBY, "ruby.mine", 1, 1, 1, 0, 1),
    Card(1, 0, GEM_TYPE.RUBY, "ruby.mine", 2, 1, 1, 0, 1),
    Card(1, 0, GEM_TYPE.RUBY, "ruby.mine", 2, 0, 1, 0, 2),
    Card(1, 0, GEM_TYPE.RUBY, "ruby.mine", 1, 0, 0, 1, 3),
    Card(1, 1, GEM_TYPE.DIAMOND, "diamond.mine", 0, 0, 4, 0, 0),
    Card(1, 0, GEM_TYPE.DIAMOND, "diamond.mine", 0, 3, 0, 0, 0),
    Card(1, 0, GEM_TYPE.DIAMOND, "diamond.mine", 3, 1, 0, 0, 1),
    Card(1, 0, GEM_TYPE.DIAMOND, "diamond.mine", 0, 2, 2, 0, 1),
    Card(1, 0, GEM_TYPE.DIAMOND, "diamond.mine", 0, 1, 1, 1, 1),
    Card(1, 0, GEM_TYPE.DIAMOND, "diamond.mine", 0, 1, 2, 1, 1),
    Card(1, 0, GEM_TYPE.DIAMOND, "diamond.mine", 0, 0, 0, 2, 1),
    Card(1, 0, GEM_TYPE.DIAMOND, "diamond.mine", 0, 2, 0, 0, 2),
]

CARDS_2 = [
    Card(2, 1, GEM_TYPE.ONYX, "onyx.camels", 3, 2, 2, 0, 0),
    Card(2, 1, GEM_TYPE.ONYX, "onyx.camels", 3, 0, 3, 0, 2),
    Card(2, 2, GEM_TYPE.ONYX, "onyx.camels", 0, 1, 4, 2, 0),
    Card(2, 2, GEM_TYPE.ONYX, "onyx.lapidary", 5, 0, 0, 0, 0),
    Card(2, 2, GEM_TYPE.ONYX, "onyx.lapidary", 0, 0, 5, 3, 0),
    Card(2, 3, GEM_TYPE.ONYX, "onyx.lapidary", 0, 0, 0, 0, 6),
    Card(2, 1, GEM_TYPE.SAPPHIRE, "sapphire.elephants", 0, 2, 2, 3, 0),
    Card(2, 1, GEM_TYPE.SAPPHIRE, "sapphire.elephants", 0, 2, 3, 0, 3),
    Card(2, 2, GEM_TYPE.SAPPHIRE, "sapphire.elephants", 5, 3, 0, 0, 0),
    Card(2, 2, GEM_TYPE.SAPPHIRE, "sapphire.lapidary", 0, 5, 0, 0, 0),
    Card(2, 2, GEM_TYPE.SAPPHIRE, "sapphire.lapidary", 2, 0, 0, 1, 4),
    Card(2, 3, GEM_TYPE.SAPPHIRE, "sapphire.lapidary", 0, 6, 0, 0, 0),
    Card(2, 2, GEM_TYPE.EMERALD, "emerald.carrack", 0, 5, 3, 0, 0),
    Card(2, 2, GEM_TYPE.EMERALD, "emerald.carrack", 0, 0, 5, 0, 0),
    Card(2, 3, GEM_TYPE.EMERALD, "emerald.carrack", 0, 0, 6, 0, 0),
    Card(2, 1, GEM_TYPE.EMERALD, "emerald.guy", 2, 3, 0, 0, 2),
    Card(2, 1, GEM_TYPE.EMERALD, "emerald.guy", 3, 0, 2, 3, 0),
    Card(2, 2, GEM_TYPE.EMERALD, "emerald.guy", 4, 2, 0, 0, 1),
    Card(2, 1, GEM_TYPE.RUBY, "ruby.felucca", 0, 3, 0, 2, 3),
    Card(2, 1, GEM_TYPE.RUBY, "ruby.felucca", 2, 0, 0, 2, 3),
    Card(2, 2, GEM_TYPE.RUBY, "ruby.felucca", 1, 4, 2, 0, 0),
    Card(2, 2, GEM_TYPE.RUBY, "ruby.lapidary", 0, 0, 0, 0, 5),
    Card(2, 2, GEM_TYPE.RUBY, "ruby.lapidary", 3, 0, 0, 0, 5),
    Card(2, 3, GEM_TYPE.RUBY, "ruby.lapidary", 0, 0, 0, 6, 0),
    Card(2, 2, GEM_TYPE.DIAMOND, "diamond.lapidary", 0, 0, 0, 5, 3),
    Card(2, 2, GEM_TYPE.DIAMOND, "diamond.lapidary", 0, 0, 0, 5, 0),
    Card(2, 3, GEM_TYPE.DIAMOND, "diamond.lapidary", 6, 0, 0, 0, 0),
    Card(2, 1, GEM_TYPE.DIAMOND, "diamond.people_in_snow", 0, 0, 3, 2, 2),
    Card(2, 1, GEM_TYPE.DIAMOND, "diamond.people_in_snow", 2, 3, 0, 3, 0),
    Card(2, 2, GEM_TYPE.DIAMOND, "diamond.people_in_snow", 0, 0, 1, 4, 2),
]

CARDS_3 = [
    Card(3, 3, GEM_TYPE.ONYX, "onyx.street1", 3, 3, 5, 3, 0),
    Card(3, 5, GEM_TYPE.ONYX, "onyx.street1", 0, 0, 0, 7, 3),
    Card(3, 4, GEM_TYPE.ONYX, "onyx.street2", 0, 0, 3, 6, 3),
    Card(3, 4, GEM_TYPE.ONYX, "onyx.street2", 0, 0, 0, 7, 0),
    Card(3, 4, GEM_TYPE.SAPPHIRE, "sapphire.diamant_shop", 6, 3, 0, 0, 3),
    Card(3, 5, GEM_TYPE.SAPPHIRE, "sapphire.diamant_shop", 7, 3, 0, 0, 0),
    Card(3, 3, GEM_TYPE.SAPPHIRE, "sapphire.venice", 3, 0, 3, 3, 5),
    Card(3, 4, GEM_TYPE.SAPPHIRE, "sapphire.venice", 7, 0, 0, 0, 0),
    Card(3, 4, GEM_TYPE.EMERALD, "emerald.bridge", 3, 6, 3, 0, 0),
    Card(3, 4, GEM_TYPE.EMERALD, "emerald.bridge", 0, 7, 0, 0, 0),
    Card(3, 3, GEM_TYPE.EMERALD, "emerald.timbered_house", 5, 3, 0, 3, 3),
    Card(3, 5, GEM_TYPE.EMERALD, "emerald.timbered_house", 0, 7, 3, 0, 0),
    Card(3, 4, GEM_TYPE.RUBY, "ruby.building", 0, 3, 6, 3, 0),
    Card(3, 5, GEM_TYPE.RUBY, "ruby.building", 0, 0, 7, 3, 0),
    Card(3, 3, GEM_TYPE.RUBY, "ruby.equestrian_statue", 3, 5, 3, 0, 3),
    Card(3, 4, GEM_TYPE.RUBY, "ruby.equestrian_statue", 0, 0, 7, 0, 0),
    Card(3, 4, GEM_TYPE.DIAMOND, "diamond.gioielleria", 3, 0, 0, 3, 6),
    Card(3, 4, GEM_TYPE.DIAMOND, "diamond.gioielleria", 0, 0, 0, 0, 7),
    Card(3, 3, GEM_TYPE.DIAMOND, "diamond.building", 0, 3, 3, 5, 3),
    Card(3, 5, GEM_TYPE.DIAMOND, "diamond.building", 3, 0, 0, 0, 7),
]

TILES = [
    Tile(3, "catherine_of_medicis", 0, 3, 3, 3, 0),
    Tile(3, "elisabeth_of_austria", 3, 3, 0, 0, 3),
    Tile(3, "isabella_of_portugal", 4, 0, 0, 0, 4),
    Tile(3, "niccolo_machiavelli", 4, 4, 0, 0, 0),
    Tile(3, "suleiman_the_magnificent", 0, 4, 4, 0, 0),
    Tile(3, "anne_of_brittany", 3, 3, 3, 0, 0),
    Tile(3, "charles_v", 3, 0, 0, 3, 3),
    Tile(3, "francis_i_of_france", 0, 0, 3, 3, 3),
    Tile(3, "henry_viii", 0, 0, 0, 4, 4),
    Tile(3, "mary", 0, 0, 4, 4, 0),
]

TOKENS_DIAMOND = [
    Token(GEM_TYPE.DIAMOND),
    Token(GEM_TYPE.DIAMOND),
    Token(GEM_TYPE.DIAMOND),
    Token(GEM_TYPE.DIAMOND),
    Token(GEM_TYPE.DIAMOND),
    Token(GEM_TYPE.DIAMOND),
    Token(GEM_TYPE.DIAMOND),
]

TOKENS_SAPPHIRE = [
    Token(GEM_TYPE.SAPPHIRE),
    Token(GEM_TYPE.SAPPHIRE),
    Token(GEM_TYPE.SAPPHIRE),
    Token(GEM_TYPE.SAPPHIRE),
    Token(GEM_TYPE.SAPPHIRE),
    Token(GEM_TYPE.SAPPHIRE),
    Token(GEM_TYPE.SAPPHIRE),
]

TOKENS_EMERALD = [
    Token(GEM_TYPE.EMERALD),
    Token(GEM_TYPE.EMERALD),
    Token(GEM_TYPE.EMERALD),
    Token(GEM_TYPE.EMERALD),
    Token(GEM_TYPE.EMERALD),
    Token(GEM_TYPE.EMERALD),
    Token(GEM_TYPE.EMERALD),
]

TOKENS_RUBY = [
    Token(GEM_TYPE.RUBY),
    Token(GEM_TYPE.RUBY),
    Token(GEM_TYPE.RUBY),
    Token(GEM_TYPE.RUBY),
    Token(GEM_TYPE.RUBY),
    Token(GEM_TYPE.RUBY),
    Token(GEM_TYPE.RUBY),
]

TOKENS_ONYX = [
    Token(GEM_TYPE.ONYX),
    Token(GEM_TYPE.ONYX),
    Token(GEM_TYPE.ONYX),
    Token(GEM_TYPE.ONYX),
    Token(GEM_TYPE.ONYX),
    Token(GEM_TYPE.ONYX),
    Token(GEM_TYPE.ONYX),
]

TOKENS_GOLD = [
    Token(GEM_TYPE.GOLD),
    Token(GEM_TYPE.GOLD),
    Token(GEM_TYPE.GOLD),
    Token(GEM_TYPE.GOLD),
    Token(GEM_TYPE.GOLD),
]

CARDS = CARDS_1 + CARDS_2 + CARDS_3
TOKENS = (
    TOKENS_DIAMOND
    + TOKENS_SAPPHIRE
    + TOKENS_EMERALD
    + TOKENS_RUBY
    + TOKENS_ONYX
    + TOKENS_GOLD
)
