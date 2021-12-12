

from __future__ import annotations

from splendor.models.uuid_object import UUIDObject
from splendor.models.boards import TableBoard
from splendor.models.boards import PlayerBoard


class Player(UUIDObject):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

class Game(UUIDObject):
    def __init__(self) -> None:
        super().__init__()
        self.table = TableBoard()
        self.players = (
            PlayerBoard(),
            PlayerBoard(),
            PlayerBoard(),
            PlayerBoard(),
        )
        self.n_players = 0
        self.n_turns = 0
        self.is_last_round = False
        self.logs = []
    
    def join(self, name: str) -> None:
        self.n_players += 1
        pass

    def start(self) -> None:
        """Sets up the board and starts the game."""
        self.table.setup(self.n_players)
