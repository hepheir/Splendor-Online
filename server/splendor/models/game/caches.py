# -*- coding: utf-8 -*-

import typing as t

from splendor.models.components import Card
from splendor.models.components import Tile
from splendor.models.components import Token
from splendor.models.game.board import CARDS
from splendor.models.game.board import TILES
from splendor.models.game.board import TOKENS


UUID_HEX = t.NewType("UUID_HEX", str)


CARDS_CACHE: t.Dict[UUID_HEX, Card] = {}
TILES_CACHE: t.Dict[UUID_HEX, Tile] = {}
TOKENS_CACHE: t.Dict[UUID_HEX, Token] = {}


def make_caches() -> None:
    for card in CARDS:
        CARDS_CACHE[card.uuid.hex] = card
    for tile in TILES:
        TILES_CACHE[tile.uuid.hex] = tile
    for token in TOKENS:
        TOKENS_CACHE[token.uuid.hex] = token


make_caches()
