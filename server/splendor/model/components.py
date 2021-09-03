from __future__ import annotations

from dataclasses import dataclass, field
from enum import IntEnum
from typing import Dict, List

from splendor.database.user import User


_T_ID = int
_T_CARD_LEVEL = int


class COIN_TYPE(IntEnum):
    DIAMOND = 0
    SAPPHIRE = 1
    EMERALD = 2
    RUBY = 3
    ONYX = 4
    GOLD = 5


class GAME_STATUS(IntEnum):
    PRE_GAME = 0
    IN_GAME = 1
    POST_GAME = 2


@dataclass
class Coin:
    coin_id: _T_ID
    coin_type: COIN_TYPE
    coin_container: CoinContainer


@dataclass
class Card:
    card_id: _T_ID
    card_level: int
    card_score: int
    card_bonus: str
    card_illustration: str
    card_cost: Cost


@dataclass
class Tile:
    tile_id: _T_ID
    tile_score: int
    tile_illustration: str
    tile_cost: Cost


@dataclass
class Cost:
    diamond: int = field(default=0)
    sapphire: int = field(default=0)
    emerald: int = field(default=0)
    ruby: int = field(default=0)
    onyx: int = field(default=0)

    def __getitem__(self, coin_type: COIN_TYPE) -> int:
        return getattr(self, coin_type.name.lower())


@dataclass
class CoinContainer:
    diamond: List[Coin] = field(default_factory=list)
    sapphire: List[Coin] = field(default_factory=list)
    emerald: List[Coin] = field(default_factory=list)
    ruby: List[Coin] = field(default_factory=list)
    onyx: List[Coin] = field(default_factory=list)
    gold: List[Coin] = field(default_factory=list)

    def __getitem__(self, coin_type: COIN_TYPE) -> List[Coin]:
        return getattr(self, coin_type.name.lower())

    def send(self, dst: CoinContainer, coin_type: COIN_TYPE, amount: int) -> None:
        assert isinstance(dst, CoinContainer)
        if len(self[coin_type]) < amount:
            print("Not enough coins.")
            return
        for i in range(amount):
            dst[coin_type].append(self[coin_type].pop())

    def get(self, src: CoinContainer, coin_type: COIN_TYPE, amount: int) -> None:
        assert isinstance(src, CoinContainer)
        src.send(self, coin_type, amount)


@dataclass
class CardSupplier:
    level: int
    drawpile: List[Card] = field(default_factory=list)
    revealed: List[Card] = field(default_factory=list)


@dataclass
class Table:
    card_supplier: Dict[_T_CARD_LEVEL, CardSupplier] = field(
        default_factory=dict)
    coin_supplier: CoinContainer = field(default_factory=CoinContainer)
    tile_supplier: List[Tile] = field(default_factory=list)


@dataclass
class Player:
    user: User
    player_coins: CoinContainer = field(default_factory=CoinContainer)
    player_tiles: List[Tile] = field(default_factory=list)
    player_cards: List[Card] = field(default_factory=list)
    player_reserved_cards: List[Card] = field(default_factory=list)


@dataclass
class Game:
    game_id: _T_ID
    game_players: List[Player] = field(default_factory=list)

    # HASH TABLE
    game_coins: Dict[_T_ID, Coin] = field(default_factory=dict)
    game_cards: Dict[_T_ID, Card] = field(default_factory=dict)
    game_tiles: Dict[_T_ID, Tile] = field(default_factory=dict)

    game_table: Table = field(default_factory=Table)
    game_status: GAME_STATUS = field(default=GAME_STATUS.PRE_GAME)
    game_turn_number: int = field(default=0)
