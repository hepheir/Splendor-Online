import typing as t

from splendor.models.enums import GEM_TYPE
from splendor.models.uuid_object import UUIDObject


CardHeaderDict = t.TypedDict('CardHeaderDict', {
    'points': int,
    'bonus': GEM_TYPE,
})

CardCostDict = t.TypedDict('CardCostDict', {
    "diamond": int,
    "sapphire": int,
    "emerald": int,
    "ruby": int,
    "onyx": int,
})

CardDict = t.TypedDict('CardDict', {
    'uuid': str,
    'level': int,
    'illustration': str,
    'header': CardHeaderDict,
    'costs': CardCostDict,
})


class Card(UUIDObject):
    """The cards used in Splendor."""

    def __init__(
        self,
        level: int,
        header_points: int,
        header_bonus: GEM_TYPE,
        cost_diamond: int,
        cost_sapphire: int,
        cost_emerald: int,
        cost_ruby: int,
        cost_onyx: int,
        illustration: str,
    ) -> None:
        super().__init__()
        self.header_points: int = header_points
        self.header_bonus: GEM_TYPE = header_bonus
        self.cost_diamond: int = cost_diamond
        self.cost_sapphire: int = cost_sapphire
        self.cost_emerald: int = cost_emerald
        self.cost_ruby: int = cost_ruby
        self.cost_onyx: int = cost_onyx
        self.level: int = level
        self.illustration: str = illustration

    def as_dict(self) -> CardDict:
        header: CardHeaderDict = {
            "points": self.header_points,
            "bonus": self.header_bonus,
        }
        costs: CardCostDict = {
            "diamond": self.cost_diamond,
            "sapphire": self.cost_sapphire,
            "emerald": self.cost_emerald,
            "ruby": self.cost_ruby,
            "onyx": self.cost_onyx,
        }
        return {
            "uuid": self.uuid.hex,
            "level": self.level,
            "illustration": self.illustration,
            "header": header,
            "costs": costs,
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
        paid += diamond - self.cost_diamond
        paid += sapphire - self.cost_sapphire
        paid += emerald - self.cost_emerald
        paid += ruby - self.cost_ruby
        paid += onyx - self.cost_onyx
        return paid == 0


class Tile(UUIDObject):
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


class Token(UUIDObject):
    def __init__(self, type: GEM_TYPE) -> None:
        super().__init__()
        self.type: GEM_TYPE = type


class CARDS:
    LEVEL_1: t.List[Card] = [
        Card(1, 1, GEM_TYPE.ONYX, 0, 4, 0, 0, 0, "onyx.mine"),
        Card(1, 0, GEM_TYPE.ONYX, 0, 0, 1, 3, 1, "onyx.mine"),
        Card(1, 0, GEM_TYPE.ONYX, 1, 1, 1, 1, 0, "onyx.mine"),
        Card(1, 0, GEM_TYPE.ONYX, 1, 2, 1, 1, 0, "onyx.mine"),
        Card(1, 0, GEM_TYPE.ONYX, 0, 0, 2, 1, 0, "onyx.mine"),
        Card(1, 0, GEM_TYPE.ONYX, 2, 2, 0, 1, 0, "onyx.mine"),
        Card(1, 0, GEM_TYPE.ONYX, 2, 0, 2, 0, 0, "onyx.mine"),
        Card(1, 0, GEM_TYPE.ONYX, 0, 0, 3, 0, 0, "onyx.mine"),
        Card(1, 1, GEM_TYPE.SAPPHIRE, 0, 0, 0, 4, 0, "sapphire.mine"),
        Card(1, 0, GEM_TYPE.SAPPHIRE, 1, 0, 1, 1, 1, "sapphire.mine"),
        Card(1, 0, GEM_TYPE.SAPPHIRE, 1, 0, 1, 2, 1, "sapphire.mine"),
        Card(1, 0, GEM_TYPE.SAPPHIRE, 0, 0, 2, 0, 2, "sapphire.mine"),
        Card(1, 0, GEM_TYPE.SAPPHIRE, 1, 0, 0, 0, 2, "sapphire.mine"),
        Card(1, 0, GEM_TYPE.SAPPHIRE, 0, 0, 0, 0, 3, "sapphire.mine"),
        Card(1, 0, GEM_TYPE.SAPPHIRE, 0, 1, 3, 1, 0, "sapphire.mine"),
        Card(1, 0, GEM_TYPE.SAPPHIRE, 1, 0, 2, 2, 0, "sapphire.mine"),
        Card(1, 1, GEM_TYPE.EMERALD, 0, 0, 0, 0, 4, "emerald.mine"),
        Card(1, 0, GEM_TYPE.EMERALD, 2, 1, 0, 0, 0, "emerald.mine"),
        Card(1, 0, GEM_TYPE.EMERALD, 1, 3, 1, 0, 0, "emerald.mine"),
        Card(1, 0, GEM_TYPE.EMERALD, 0, 2, 0, 2, 0, "emerald.mine"),
        Card(1, 0, GEM_TYPE.EMERALD, 0, 0, 0, 3, 0, "emerald.mine"),
        Card(1, 0, GEM_TYPE.EMERALD, 1, 1, 0, 1, 1, "emerald.mine"),
        Card(1, 0, GEM_TYPE.EMERALD, 1, 1, 0, 1, 2, "emerald.mine"),
        Card(1, 0, GEM_TYPE.EMERALD, 0, 1, 0, 2, 2, "emerald.mine"),
        Card(1, 1, GEM_TYPE.RUBY, 4, 0, 0, 0, 0, "ruby.mine"),
        Card(1, 0, GEM_TYPE.RUBY, 3, 0, 0, 0, 0, "ruby.mine"),
        Card(1, 0, GEM_TYPE.RUBY, 0, 2, 1, 0, 0, "ruby.mine"),
        Card(1, 0, GEM_TYPE.RUBY, 2, 0, 0, 2, 0, "ruby.mine"),
        Card(1, 0, GEM_TYPE.RUBY, 1, 1, 1, 0, 1, "ruby.mine"),
        Card(1, 0, GEM_TYPE.RUBY, 2, 1, 1, 0, 1, "ruby.mine"),
        Card(1, 0, GEM_TYPE.RUBY, 2, 0, 1, 0, 2, "ruby.mine"),
        Card(1, 0, GEM_TYPE.RUBY, 1, 0, 0, 1, 3, "ruby.mine"),
        Card(1, 1, GEM_TYPE.DIAMOND, 0, 0, 4, 0, 0, "diamond.mine"),
        Card(1, 0, GEM_TYPE.DIAMOND, 0, 3, 0, 0, 0, "diamond.mine"),
        Card(1, 0, GEM_TYPE.DIAMOND, 3, 1, 0, 0, 1, "diamond.mine"),
        Card(1, 0, GEM_TYPE.DIAMOND, 0, 2, 2, 0, 1, "diamond.mine"),
        Card(1, 0, GEM_TYPE.DIAMOND, 0, 1, 1, 1, 1, "diamond.mine"),
        Card(1, 0, GEM_TYPE.DIAMOND, 0, 1, 2, 1, 1, "diamond.mine"),
        Card(1, 0, GEM_TYPE.DIAMOND, 0, 0, 0, 2, 1, "diamond.mine"),
        Card(1, 0, GEM_TYPE.DIAMOND, 0, 2, 0, 0, 2, "diamond.mine"),
    ]

    LEVEL_2: t.List[Card] = [
        Card(2, 1, GEM_TYPE.ONYX, 3, 2, 2, 0, 0, "onyx.camels"),
        Card(2, 1, GEM_TYPE.ONYX, 3, 0, 3, 0, 2, "onyx.camels"),
        Card(2, 2, GEM_TYPE.ONYX, 0, 1, 4, 2, 0, "onyx.camels"),
        Card(2, 2, GEM_TYPE.ONYX, 5, 0, 0, 0, 0, "onyx.lapidary"),
        Card(2, 2, GEM_TYPE.ONYX, 0, 0, 5, 3, 0, "onyx.lapidary"),
        Card(2, 3, GEM_TYPE.ONYX, 0, 0, 0, 0, 6, "onyx.lapidary"),
        Card(2, 1, GEM_TYPE.SAPPHIRE, 0, 2, 2, 3, 0, "sapphire.elephants"),
        Card(2, 1, GEM_TYPE.SAPPHIRE, 0, 2, 3, 0, 3, "sapphire.elephants"),
        Card(2, 2, GEM_TYPE.SAPPHIRE, 5, 3, 0, 0, 0, "sapphire.elephants"),
        Card(2, 2, GEM_TYPE.SAPPHIRE, 0, 5, 0, 0, 0, "sapphire.lapidary"),
        Card(2, 2, GEM_TYPE.SAPPHIRE, 2, 0, 0, 1, 4, "sapphire.lapidary"),
        Card(2, 3, GEM_TYPE.SAPPHIRE, 0, 6, 0, 0, 0, "sapphire.lapidary"),
        Card(2, 2, GEM_TYPE.EMERALD, 0, 5, 3, 0, 0, "emerald.carrack"),
        Card(2, 2, GEM_TYPE.EMERALD, 0, 0, 5, 0, 0, "emerald.carrack"),
        Card(2, 3, GEM_TYPE.EMERALD, 0, 0, 6, 0, 0, "emerald.carrack"),
        Card(2, 1, GEM_TYPE.EMERALD, 2, 3, 0, 0, 2, "emerald.guy"),
        Card(2, 1, GEM_TYPE.EMERALD, 3, 0, 2, 3, 0, "emerald.guy"),
        Card(2, 2, GEM_TYPE.EMERALD, 4, 2, 0, 0, 1, "emerald.guy"),
        Card(2, 1, GEM_TYPE.RUBY, 0, 3, 0, 2, 3, "ruby.felucca"),
        Card(2, 1, GEM_TYPE.RUBY, 2, 0, 0, 2, 3, "ruby.felucca"),
        Card(2, 2, GEM_TYPE.RUBY, 1, 4, 2, 0, 0, "ruby.felucca"),
        Card(2, 2, GEM_TYPE.RUBY, 0, 0, 0, 0, 5, "ruby.lapidary"),
        Card(2, 2, GEM_TYPE.RUBY, 3, 0, 0, 0, 5, "ruby.lapidary"),
        Card(2, 3, GEM_TYPE.RUBY, 0, 0, 0, 6, 0, "ruby.lapidary"),
        Card(2, 2, GEM_TYPE.DIAMOND, 0, 0, 0, 5, 3, "diamond.lapidary"),
        Card(2, 2, GEM_TYPE.DIAMOND, 0, 0, 0, 5, 0, "diamond.lapidary"),
        Card(2, 3, GEM_TYPE.DIAMOND, 6, 0, 0, 0, 0, "diamond.lapidary"),
        Card(2, 1, GEM_TYPE.DIAMOND, 0, 0, 3, 2, 2, "diamond.people_in_snow"),
        Card(2, 1, GEM_TYPE.DIAMOND, 2, 3, 0, 3, 0, "diamond.people_in_snow"),
        Card(2, 2, GEM_TYPE.DIAMOND, 0, 0, 1, 4, 2, "diamond.people_in_snow"),
    ]

    LEVEL_3: t.List[Card] = [
        Card(3, 3, GEM_TYPE.ONYX, 3, 3, 5, 3, 0, "onyx.street1"),
        Card(3, 5, GEM_TYPE.ONYX, 0, 0, 0, 7, 3, "onyx.street1"),
        Card(3, 4, GEM_TYPE.ONYX, 0, 0, 3, 6, 3, "onyx.street2"),
        Card(3, 4, GEM_TYPE.ONYX, 0, 0, 0, 7, 0, "onyx.street2"),
        Card(3, 4, GEM_TYPE.SAPPHIRE, 6, 3, 0, 0, 3, "sapphire.diamant_shop"),
        Card(3, 5, GEM_TYPE.SAPPHIRE, 7, 3, 0, 0, 0, "sapphire.diamant_shop"),
        Card(3, 3, GEM_TYPE.SAPPHIRE, 3, 0, 3, 3, 5, "sapphire.venice"),
        Card(3, 4, GEM_TYPE.SAPPHIRE, 7, 0, 0, 0, 0, "sapphire.venice"),
        Card(3, 4, GEM_TYPE.EMERALD, 3, 6, 3, 0, 0, "emerald.bridge"),
        Card(3, 4, GEM_TYPE.EMERALD, 0, 7, 0, 0, 0, "emerald.bridge"),
        Card(3, 3, GEM_TYPE.EMERALD, 5, 3, 0, 3, 3, "emerald.timbered_house"),
        Card(3, 5, GEM_TYPE.EMERALD, 0, 7, 3, 0, 0, "emerald.timbered_house"),
        Card(3, 4, GEM_TYPE.RUBY, 0, 3, 6, 3, 0, "ruby.building"),
        Card(3, 5, GEM_TYPE.RUBY, 0, 0, 7, 3, 0, "ruby.building"),
        Card(3, 3, GEM_TYPE.RUBY, 3, 5, 3, 0, 3, "ruby.equestrian_statue"),
        Card(3, 4, GEM_TYPE.RUBY, 0, 0, 7, 0, 0, "ruby.equestrian_statue"),
        Card(3, 4, GEM_TYPE.DIAMOND, 3, 0, 0, 3, 6, "diamond.gioielleria"),
        Card(3, 4, GEM_TYPE.DIAMOND, 0, 0, 0, 0, 7, "diamond.gioielleria"),
        Card(3, 3, GEM_TYPE.DIAMOND, 0, 3, 3, 5, 3, "diamond.building"),
        Card(3, 5, GEM_TYPE.DIAMOND, 3, 0, 0, 0, 7, "diamond.building"),
    ]


class TOKENS:
    DIAMOND: t.List[Token] = [
        Token(GEM_TYPE.DIAMOND),
        Token(GEM_TYPE.DIAMOND),
        Token(GEM_TYPE.DIAMOND),
        Token(GEM_TYPE.DIAMOND),
        Token(GEM_TYPE.DIAMOND),
        Token(GEM_TYPE.DIAMOND),
        Token(GEM_TYPE.DIAMOND),
    ]

    SAPPHIRE: t.List[Token] = [
        Token(GEM_TYPE.SAPPHIRE),
        Token(GEM_TYPE.SAPPHIRE),
        Token(GEM_TYPE.SAPPHIRE),
        Token(GEM_TYPE.SAPPHIRE),
        Token(GEM_TYPE.SAPPHIRE),
        Token(GEM_TYPE.SAPPHIRE),
        Token(GEM_TYPE.SAPPHIRE),
    ]

    EMERALD: t.List[Token] = [
        Token(GEM_TYPE.EMERALD),
        Token(GEM_TYPE.EMERALD),
        Token(GEM_TYPE.EMERALD),
        Token(GEM_TYPE.EMERALD),
        Token(GEM_TYPE.EMERALD),
        Token(GEM_TYPE.EMERALD),
        Token(GEM_TYPE.EMERALD),
    ]

    RUBY: t.List[Token] = [
        Token(GEM_TYPE.RUBY),
        Token(GEM_TYPE.RUBY),
        Token(GEM_TYPE.RUBY),
        Token(GEM_TYPE.RUBY),
        Token(GEM_TYPE.RUBY),
        Token(GEM_TYPE.RUBY),
        Token(GEM_TYPE.RUBY),
    ]

    ONYX: t.List[Token] = [
        Token(GEM_TYPE.ONYX),
        Token(GEM_TYPE.ONYX),
        Token(GEM_TYPE.ONYX),
        Token(GEM_TYPE.ONYX),
        Token(GEM_TYPE.ONYX),
        Token(GEM_TYPE.ONYX),
        Token(GEM_TYPE.ONYX),
    ]

    GOLD: t.List[Token] = [
        Token(GEM_TYPE.GOLD),
        Token(GEM_TYPE.GOLD),
        Token(GEM_TYPE.GOLD),
        Token(GEM_TYPE.GOLD),
        Token(GEM_TYPE.GOLD),
    ]


TILES: t.List[Tile] = [
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
