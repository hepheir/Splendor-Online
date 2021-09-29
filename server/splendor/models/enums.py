# -*- coding: utf-8 -*-

from enum import auto, IntEnum


class GEM_TYPE(IntEnum):
    DIAMOND = auto()
    SAPPHIRE = auto()
    EMERALD = auto()
    RUBY = auto()
    ONYX = auto()
    GOLD = auto()


class GAME_STATE(IntEnum):
    PRE_GAME = auto()
    SETTING_UP = auto()


class PLAYER_STATE(IntEnum):
    WAITING = auto()
    PLAYING = auto()
