# -*- coding: utf-8 -*-

from uuid import UUID
from uuid import uuid4


class Item(object):
    def __init__(self) -> None:
        super().__init__()
        self.uuid: UUID = uuid4()
