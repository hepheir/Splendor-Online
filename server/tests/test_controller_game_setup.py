from typing import List

import pytest

from splendor.controller.game_setup import add_player, create_new_game, setup_cards, setup_coins, setup_tiles
from splendor.database.user import User, get_user_by_id
from splendor.model.components import CardSupplier, Game, Player


@pytest.fixture
def my_game() -> Game:
    return create_new_game("0001")


@pytest.fixture
def my_users() -> List[User]:
    return [get_user_by_id(user_id+1) for user_id in range(8)]


def test_game_id(my_game: Game):
    assert my_game.game_id == "0001"


def test_add_players(my_game: Game, my_users: List[User]):
    for user in my_users[:4]:
        add_player(my_game, user)
    assert len(my_game.game_players) == 4
    for player, user in zip(my_game.game_players, my_users):
        assert isinstance(player, Player)
        assert player.user is user


def test_add_same_player(my_game: Game, my_users: List[User]):
    add_player(my_game, my_users[0])
    add_player(my_game, my_users[0])
    assert len(my_game.game_players) == 1


def test_setup_coins_for_4_players(my_game: Game, my_users: List[User]):
    for user in my_users[:4]:
        add_player(my_game, user)
    setup_coins(my_game)
    assert len(my_game.game_table.coin_supplier.diamond) == 7
    assert len(my_game.game_table.coin_supplier.sapphire) == 7
    assert len(my_game.game_table.coin_supplier.emerald) == 7
    assert len(my_game.game_table.coin_supplier.ruby) == 7
    assert len(my_game.game_table.coin_supplier.onyx) == 7
    assert len(my_game.game_table.coin_supplier.gold) == 5
    assert len(my_game.game_coins) == 40


def test_setup_coins_for_3_players(my_game: Game, my_users: List[User]):
    for user in my_users[:3]:
        add_player(my_game, user)
    setup_coins(my_game)
    assert len(my_game.game_table.coin_supplier.diamond) == 5
    assert len(my_game.game_table.coin_supplier.sapphire) == 5
    assert len(my_game.game_table.coin_supplier.emerald) == 5
    assert len(my_game.game_table.coin_supplier.ruby) == 5
    assert len(my_game.game_table.coin_supplier.onyx) == 5
    assert len(my_game.game_table.coin_supplier.gold) == 5
    assert len(my_game.game_coins) == 30


def test_setup_coins_for_2_players(my_game: Game, my_users: List[User]):
    for user in my_users[:2]:
        add_player(my_game, user)
    setup_coins(my_game)
    assert len(my_game.game_table.coin_supplier.diamond) == 4
    assert len(my_game.game_table.coin_supplier.sapphire) == 4
    assert len(my_game.game_table.coin_supplier.emerald) == 4
    assert len(my_game.game_table.coin_supplier.ruby) == 4
    assert len(my_game.game_table.coin_supplier.onyx) == 4
    assert len(my_game.game_table.coin_supplier.gold) == 5
    assert len(my_game.game_coins) == 25


def test_setup_cards(my_game: Game, my_users: List[User]):
    for user in my_users[:4]:
        add_player(my_game, user)
    setup_cards(my_game)
    assert len(my_game.game_cards) == 90

    assert isinstance(my_game.game_table.card_supplier[1], CardSupplier)
    assert my_game.game_table.card_supplier[1].level == 1
    assert len(my_game.game_table.card_supplier[1].drawpile) == 40-4
    assert len(my_game.game_table.card_supplier[1].revealed) == 4

    assert isinstance(my_game.game_table.card_supplier[2], CardSupplier)
    assert my_game.game_table.card_supplier[2].level == 2
    assert len(my_game.game_table.card_supplier[2].drawpile) == 30-4
    assert len(my_game.game_table.card_supplier[2].revealed) == 4

    assert isinstance(my_game.game_table.card_supplier[3], CardSupplier)
    assert my_game.game_table.card_supplier[3].level == 3
    assert len(my_game.game_table.card_supplier[3].drawpile) == 20-4
    assert len(my_game.game_table.card_supplier[3].revealed) == 4


def test_setup_tiles(my_game: Game, my_users: List[User]):
    for user in my_users[:4]:
        add_player(my_game, user)
    setup_tiles(my_game)
    assert len(my_game.game_tiles) == 5
