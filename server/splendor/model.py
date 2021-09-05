from enum import IntEnum, auto


class COMPONENT_TYPE(IntEnum):
    CARD = auto()
    TILE = auto()
    COIN = auto()


class COIN_TYPE(IntEnum):
    GOLD = 0
    DIAMOND = 1
    SAPPHIRE = 2
    EMERALD = 3
    RUBY = 4
    ONYX = 5


class GAME_STATE(IntEnum):
    PRE_GAME = auto()
    START_GAME = auto()
    END_GAME = auto()
    BEGIN_ROUND = auto()
    END_ROUND = auto()
    BEGIN_TURN = auto()
    END_TURN = auto()
    WAITING_FOR_PRE_ACTION = auto()
    WAITING_FOR_POST_ACTION = auto()
