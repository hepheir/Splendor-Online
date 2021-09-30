# -*- coding: utf-8 -*-

from __future__ import annotations

import typing as t
from uuid import UUID

from splendor.models.containers import CardContainer
from splendor.models.containers import TileContainer
from splendor.models.containers import TokenContainer
from splendor.models.components import Card
from splendor.models.enums import GAME_STATE, GEM_TYPE
from splendor.models.enums import PLAYER_STATE
from splendor.models.game.board import Board
from splendor.models.items import Item


class Player(Item):
    def __init__(self, game: Game, name: str) -> None:
        super().__init__()
        self.name: str = name
        self.game: Game = game
        self.state: PLAYER_STATE = PLAYER_STATE.WAITING

        self.reserved: t.List[Card] = []
        self.cards: CardContainer = CardContainer()
        self.tiles: TileContainer = TileContainer()
        self.tokens: TokenContainer = TokenContainer()
        self.tokens_taken: int = 0

    def as_dict(self) -> t.Dict[str, t.Any]:
        return {
            "uuid": self.uuid,
            "name": self.name,
            "is_playing": self.state is PLAYER_STATE.PLAYING,
            "points": self.points(),
            "tiles": self.tiles.as_dict(),
            "cards": self.cards.as_dict(),
            "tokens": self.tokens.as_dict(),
            "reserved": self.reserved,
        }

    def count_points(self) -> int:
        return self.cards.points + self.tiles.points

    def action_buy(self, card_uuid: UUID) -> None:
        pass

    def action_take(self, gem_type: GEM_TYPE) -> None:
        pass


class Game(Item):
    def __init__(self, host: Player) -> None:
        super().__init__()
        self.host: Player = host
        self.players: t.List[Player] = [host]
        self.state: GAME_STATE = GAME_STATE.PRE_GAME
        self.board: Board = Board()

        self.log: t.List[str] = []
        self.turns: int = 0

    def current_player(self) -> Player:
        return self.players[self.turns % len(self.players)]

    def start_game(self) -> None:
        if self.state is not GAME_STATE.PRE_GAME:
            raise Exception("Game cannot be started.")

        self.state = GAME_STATE.SETTING_UP
        self.board.setup(n_players=len(self.players))
