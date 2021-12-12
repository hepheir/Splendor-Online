

from __future__ import annotations

import typing as t
from random import shuffle

from splendor.models.components import CARDS
from splendor.models.components import TILES
from splendor.models.components import TOKENS
from splendor.models.uuid_object import UUID
from splendor.models.uuid_object import UUIDObject


class Slot(UUIDObject):
    def __init__(self) -> None:
        super().__init__()
        self.data = None

    def as_dict(self) -> t.Union[str, None]:
        """Returns the hex-string of `UUID` of containing item.
        If there is no item in slot, this would return `None`.
        """
        if self.data is None:
            return None
        else:
            return self.data.hex

    def clear(self) -> None:
        self.delitem()

    def setitem(self, uuid: UUID) -> None:
        self.data = uuid

    def getitem(self) -> UUID:
        return self.data

    def delitem(self) -> None:
        self.data = None

    def popitem(self) -> UUID:
        item = self.getitem()
        self.delitem()
        return item


class StackSlot(UUIDObject):
    def __init__(self) -> None:
        super().__init__()
        self.data: t.List[UUID] = []
        self.iter_counter = 0

    def __len__(self) -> int:
        return len(self.data)

    def __iter__(self) -> t.Iterator[UUID]:
        self.iter_counter = 0
        return self

    def __next__(self) -> UUID:
        if self.iter_counter < len(self):
            item = self.data[self.iter_counter]
            self.iter_counter += 1
            return item
        else:
            raise StopIteration

    def as_dict(self) -> t.Tuple[t.Union[str, None]]:
        """Returns a tuple of hex-strings of `UUID` of containing item.
        If there is no item in slot, this would return `None`.
        """
        return tuple(map(lambda uuid: uuid.hex, self))

    def clear(self) -> None:
        self.data.clear()

    def pushitem(self, uuid: UUID) -> None:
        self.data.append(uuid)

    def popitem(self) -> UUID:
        self.data.pop()

    def extend(self, iterable: t.Iterable[UUID]) -> None:
        self.data.extend(iterable)


class Board(UUIDObject):
    def __init__(self) -> None:
        super().__init__()
        self.slots: t.List[t.Union[Slot, StackSlot]] = []


class PlayerBoard(Board):
    def __init__(self) -> None:
        super().__init__()
        self.slots = (
            StackSlot(),
            StackSlot(),
            StackSlot(),
            StackSlot(),
            StackSlot(),
            StackSlot(),
            StackSlot(),
            StackSlot(),
            StackSlot(),
            StackSlot(),
            StackSlot(),
            StackSlot(),
            Slot(),
            Slot(),
            Slot(),
            Slot(),
            Slot(),
            Slot(),
            Slot(),
            Slot(),
        )

    def as_dict(self) -> t.Dict:
        return {
            "tokens": {
                "diamond": len(self.slots[0]),
                "sapphire": len(self.slots[1]),
                "emerald": len(self.slots[2]),
                "ruby": len(self.slots[3]),
                "onyx": len(self.slots[4]),
                "gold": len(self.slots[5]),
            },
            "cards": {
                "diamond": self.slots[6].as_dict(),
                "sapphire": self.slots[7].as_dict(),
                "emerald": self.slots[8].as_dict(),
                "ruby": self.slots[9].as_dict(),
                "onyx": self.slots[10].as_dict(),
                "reserves": [
                    self.slots[16].as_dict(),
                    self.slots[17].as_dict(),
                    self.slots[18].as_dict(),
                ],
            },
            "tiles": [
                self.slots[11].as_dict(),
                self.slots[12].as_dict(),
                self.slots[13].as_dict(),
                self.slots[14].as_dict(),
                self.slots[15].as_dict(),
            ],
        }

    def clear(self) -> None:
        for slot in self.slots:
            slot.clear()


class TableBoard(Board):
    def __init__(self) -> None:
        super().__init__()
        self.slots = (
            StackSlot(),
            StackSlot(),
            StackSlot(),
            StackSlot(),
            StackSlot(),
            StackSlot(),
            StackSlot(),
            Slot(),
            Slot(),
            Slot(),
            Slot(),
            StackSlot(),
            Slot(),
            Slot(),
            Slot(),
            Slot(),
            StackSlot(),
            Slot(),
            Slot(),
            Slot(),
            Slot(),
            Slot(),
            Slot(),
            Slot(),
            Slot(),
            Slot(),
        )

    def as_dict(self) -> t.Dict:
        return {
            "tokens": {
                "diamond": len(self.slots[0]),
                "sapphire": len(self.slots[1]),
                "emerald": len(self.slots[2]),
                "ruby": len(self.slots[3]),
                "onyx": len(self.slots[4]),
                "gold": len(self.slots[5]),
            },
            "cards": {
                "1": [
                    len(self.slots[6].as_dict()),
                    self.slots[7].as_dict(),
                    self.slots[8].as_dict(),
                    self.slots[9].as_dict(),
                    self.slots[10].as_dict(),
                ],
                "2": [
                    len(self.slots[11].as_dict()),
                    self.slots[12].as_dict(),
                    self.slots[13].as_dict(),
                    self.slots[14].as_dict(),
                    self.slots[15].as_dict(),
                ],
                "3": [
                    len(self.slots[16].as_dict()),
                    self.slots[17].as_dict(),
                    self.slots[18].as_dict(),
                    self.slots[19].as_dict(),
                    self.slots[20].as_dict(),
                ],
            },
            "tiles": [
                self.slots[21].as_dict(),
                self.slots[22].as_dict(),
                self.slots[23].as_dict(),
                self.slots[24].as_dict(),
                self.slots[25].as_dict(),
            ],
        }

    def clear(self) -> None:
        for slot in self.slots:
            slot.clear()

    def setup(self, n_players: int) -> None:
        self.clear()
        self.setup_cards()
        self.setup_tiles(n_players)
        self.setup_tokens(n_players)

    def setup_cards(self) -> None:
        shuffle(CARDS.LEVEL_1)
        for i in range(4):
            self.slots[7 + i].setitem(CARDS.LEVEL_1[i].uuid)
        for i in range(4, 40):
            self.slots[6].pushitem(CARDS.LEVEL_1[i].uuid)
        shuffle(CARDS.LEVEL_2)
        for i in range(4):
            self.slots[12 + i].setitem(CARDS.LEVEL_2[i].uuid)
        for i in range(4, 30):
            self.slots[11].pushitem(CARDS.LEVEL_2[i].uuid)
        shuffle(CARDS.LEVEL_3)
        for i in range(4):
            self.slots[17 + i].setitem(CARDS.LEVEL_3[i].uuid)
        for i in range(4, 20):
            self.slots[16].pushitem(CARDS.LEVEL_3[i].uuid)

    def setup_tiles(self, n_players: int) -> None:
        shuffle(TILES)
        for i in range(n_players + 1):
            self.slots[21 + i].setitem(TILES[i].uuid)

    def setup_tokens(self, n_players: int) -> None:
        if n_players == 2:
            n_tokens = 4
        elif n_players == 3:
            n_tokens = 5
        else:
            n_tokens = 7
        for i in range(n_tokens):
            self.slots[0].pushitem(TOKENS.DIAMOND[i].uuid)
            self.slots[1].pushitem(TOKENS.SAPPHIRE[i].uuid)
            self.slots[2].pushitem(TOKENS.EMERALD[i].uuid)
            self.slots[3].pushitem(TOKENS.RUBY[i].uuid)
            self.slots[4].pushitem(TOKENS.ONYX[i].uuid)
        for i in range(5):
            self.slots[5].pushitem(TOKENS.GOLD[i].uuid)
