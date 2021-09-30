# -*- coding: utf-8 -*-

from __future__ import annotations

import typing as t

from splendor.models.components import Card
from splendor.models.components import Tile
from splendor.models.components import Token
from splendor.models.enums import GEM_TYPE
from splendor.models.items import Item


class _GemContainer(Item):
    def __init__(self) -> None:
        super().__init__()
        self.diamond: t.List = []
        self.sapphire: t.List = []
        self.emerald: t.List = []
        self.ruby: t.List = []
        self.onyx: t.List = []
        self.gold: t.List = []

    def __getitem__(self, key: GEM_TYPE) -> t.List[Token]:
        gem_type = key.name.lower()
        if gem_type not in self.__dict__:
            raise KeyError(f"Couldn't find attribute {key}")
        return getattr(self, gem_type)

    def amount(self, type: GEM_TYPE) -> int:
        return len(self[type])

    def insert(self, type: GEM_TYPE, item: t.Any) -> None:
        self[type].append(item)

    def pop(self, type: GEM_TYPE) -> t.Any:
        return self[type].pop()

    def total_amount(self) -> int:
        cnt = 0
        for gem_type in GEM_TYPE:
            cnt += self.amount(gem_type)
        return cnt


class CardContainer(_GemContainer):
    def __init__(self) -> None:
        super().__init__()
        self.diamond: t.List[Card]
        self.sapphire: t.List[Card]
        self.emerald: t.List[Card]
        self.ruby: t.List[Card]
        self.onyx: t.List[Card]
        self.points: int = 0

    def __getitem__(self, key: GEM_TYPE) -> t.List[Token]:
        if key is GEM_TYPE.GOLD:
            raise KeyError("Cards with gold bonuses are not supported.")
        return super().__getitem__(key)

    def as_dict(self) -> t.Dict:
        return {
            "diamond": self.amount(GEM_TYPE.DIAMOND),
            "sapphire": self.amount(GEM_TYPE.SAPPHIRE),
            "emerald": self.amount(GEM_TYPE.EMERALD),
            "ruby": self.amount(GEM_TYPE.RUBY),
            "onyx": self.amount(GEM_TYPE.ONYX),
            "points": self.points,
        }

    def insert(self, card: Card) -> None:
        super().insert(card.bonus, card)
        self.points += card.points

    def pop(self) -> Card:
        raise NotImplementedError("Cannot pop a card.")


class TileContainer(Item):
    def __init__(self) -> None:
        super().__init__()
        self.tiles: t.List[Tile] = []
        self.points = 0

    def as_dict(self) -> t.Dict:
        return {
            "tiles": self.tiles,
            "points": self.points,
        }

    def insert(self, tile: Tile) -> None:
        self.tiles.append(tile)
        self.points += tile.points


class TokenContainer(_GemContainer):
    def __init__(self) -> None:
        super().__init__()
        self.diamond: t.List[Token]
        self.sapphire: t.List[Token]
        self.emerald: t.List[Token]
        self.ruby: t.List[Token]
        self.onyx: t.List[Token]
        self.gold: t.List[Token]

    def as_dict(self) -> t.Dict:
        return {
            "diamond": self.amount(GEM_TYPE.DIAMOND),
            "sapphire": self.amount(GEM_TYPE.SAPPHIRE),
            "emerald": self.amount(GEM_TYPE.EMERALD),
            "ruby": self.amount(GEM_TYPE.RUBY),
            "onyx": self.amount(GEM_TYPE.ONYX),
            "gold": self.amount(GEM_TYPE.GOLD),
        }

    def insert(self, token: Token) -> None:
        super().insert(token.type, token)

    def pop(self, type: GEM_TYPE) -> Token:
        return super().pop(type)
