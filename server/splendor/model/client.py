from __future__ import annotations

from dataclasses import dataclass
from typing import List


TileSupplier = List[int]

@dataclass
class CardSupplier:
    level: int
    drawables: int
    revealed: List[int]


@dataclass
class CoinSupplier:
    diamond: int
    sapphire: int
    emerald: int
    ruby: int
    onyx: int
    gold: int


@dataclass
class PlayerSummary:
    player_id: int
    player_name: str
    player_score: int
    player_cards: List[int]
    player_tiles: List[int]
    player_card_counts: CoinSupplier
    player_coin_counts: CoinSupplier


@dataclass
class Table:
    tile_supplier: TileSupplier
    card_suppliers: List[CardSupplier]
    coin_supplier: CoinSupplier
    players: List[PlayerSummary]


def cast_table(game) -> Table:
    return Table(
        tile_supplier=[],
        card_suppliers=[],
        coin_supplier=CoinSupplier(

        ),
        players=[]
    )
