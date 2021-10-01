# -*- coding: utf-8 -*-

from __future__ import annotations

from splendor.models.uuid_object import UUIDObject
from splendor.models.boards import TableBoard


class Game(UUIDObject):
    def __init__(self) -> None:
        super().__init__()
        self.table = TableBoard()
