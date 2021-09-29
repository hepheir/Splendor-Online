# -*- coding: utf-8 -*-

import typing as t

from splendor.models.enums import GEM_TYPE
from splendor.models.items import Item


class Card(Item):
    def __init__(
        self,
        level: int,
        points: int,
        bonus: GEM_TYPE,
        illustration: str,
        diamond: int,
        sapphire: int,
        emerald: int,
        ruby: int,
        onyx: int,
    ) -> None:
        super().__init__()
        self.level: int = level
        self.points: int = points
        self.bonus: GEM_TYPE = bonus
        self.illustration: str = illustration
        self.diamond: int = diamond
        self.sapphire: int = sapphire
        self.emerald: int = emerald
        self.ruby: int = ruby
        self.onyx: int = onyx

    def as_dict(self) -> t.Dict[str, t.Any]:
        return {
            "uuid": self.uuid.hex,
            "level": self.level,
            "points": self.points,
            "bonus": self.bonus,
            "costs": {
                "diamond": self.diamond,
                "sapphire": self.sapphire,
                "emerald": self.emerald,
                "ruby": self.ruby,
                "onyx": self.onyx,
            },
            "illustration": self.illustration,
        }

    def is_buyable(
        self,
        diamond: int,
        sapphire: int,
        emerald: int,
        ruby: int,
        onyx: int,
        gold: int,
    ) -> bool:
        paid = gold
        paid += diamond - self.diamond
        paid += sapphire - self.sapphire
        paid += emerald - self.emerald
        paid += ruby - self.ruby
        paid += onyx - self.onyx
        return paid == 0


class Tile(Item):
    def __init__(
        self,
        points: int,
        illustration: str,
        diamond: int,
        sapphire: int,
        emerald: int,
        ruby: int,
        onyx: int,
    ) -> None:
        super().__init__()
        self.points: int = points
        self.illustration: str = illustration
        self.diamond: int = diamond
        self.sapphire: int = sapphire
        self.emerald: int = emerald
        self.ruby: int = ruby
        self.onyx: int = onyx

    def as_dict(self) -> t.Dict[str, t.Any]:
        return {
            "uuid": self.uuid.hex,
            "points": self.points,
            "requirements": {
                "diamond": self.diamond,
                "sapphire": self.sapphire,
                "emerald": self.emerald,
                "ruby": self.ruby,
                "onyx": self.onyx,
            },
            "illustration": self.illustration,
        }


class Token(Item):
    def __init__(self, type: GEM_TYPE) -> None:
        super().__init__()
        self.type: GEM_TYPE = type
