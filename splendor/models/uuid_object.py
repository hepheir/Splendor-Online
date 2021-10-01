# -*- coding: utf-8 -*-

from __future__ import annotations

import typing as t

from uuid import UUID
from uuid import uuid4


CACHES: t.Dict[str, UUIDObject] = {}


class UUIDObject(object):
    def __init__(self) -> None:
        super().__init__()
        self.uuid: UUID = uuid4()

    def make_cache(self) -> None:
        CACHES[self.uuid.hex] = self


def get_by_uuid(uuid: UUID) -> UUIDObject:
    """Get an `UUIDObject` with given `UUID`.

    The object must be cached using `UUIDObject.make_cache()`.
    """
    if uuid.hex not in CACHES:
        raise KeyError("Object with uuid does not exist.")
    else:
        return CACHES[uuid.hex]
