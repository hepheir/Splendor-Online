from typing import List

import pytest

from splendor import controller, database, model


@pytest.fixture
def my_game() -> model.components.Game:
    return controller.create_new_game("test.controller_game_setup")


@pytest.fixture
def my_users() -> List[database.user.User]:
    return [database.user.get_user_by_id(user_id+1) for user_id in range(8)]


def test_game_id(my_game: model.components.Game):
    assert my_game.game_id == "test.controller_game_setup"


def test_add_players(my_game: model.components.Game, my_users: List[database.user.User]):
    for user in my_users[:4]:
        controller.add_player(my_game, user)
    assert len(my_game.game_players) == 4
    for player, user in zip(my_game.game_players, my_users):
        assert isinstance(player, model.components.Player)
        assert player.user is user


def test_add_same_player(my_game: model.components.Game, my_users: List[database.user.User]):
    controller.add_player(my_game, my_users[0])
    controller.add_player(my_game, my_users[0])
    assert len(my_game.game_players) == 1


def test_setup_coins_for_4_players(my_game: model.components.Game, my_users: List[database.user.User]):
    for user in my_users[:4]:
        controller.add_player(my_game, user)
    controller.game_setup.setup_coins(my_game)
    assert len(my_game.game_table.coin_supplier.diamond) == 7
    assert len(my_game.game_table.coin_supplier.sapphire) == 7
    assert len(my_game.game_table.coin_supplier.emerald) == 7
    assert len(my_game.game_table.coin_supplier.ruby) == 7
    assert len(my_game.game_table.coin_supplier.onyx) == 7
    assert len(my_game.game_table.coin_supplier.gold) == 5


def test_setup_coins_for_3_players(my_game: model.components.Game, my_users: List[database.user.User]):
    for user in my_users[:3]:
        controller.add_player(my_game, user)
    controller.game_setup.setup_coins(my_game)
    assert len(my_game.game_table.coin_supplier.diamond) == 5
    assert len(my_game.game_table.coin_supplier.sapphire) == 5
    assert len(my_game.game_table.coin_supplier.emerald) == 5
    assert len(my_game.game_table.coin_supplier.ruby) == 5
    assert len(my_game.game_table.coin_supplier.onyx) == 5
    assert len(my_game.game_table.coin_supplier.gold) == 5


def test_setup_coins_for_2_players(my_game: model.components.Game, my_users: List[database.user.User]):
    for user in my_users[:2]:
        controller.add_player(my_game, user)
    controller.game_setup.setup_coins(my_game)
    assert len(my_game.game_table.coin_supplier.diamond) == 4
    assert len(my_game.game_table.coin_supplier.sapphire) == 4
    assert len(my_game.game_table.coin_supplier.emerald) == 4
    assert len(my_game.game_table.coin_supplier.ruby) == 4
    assert len(my_game.game_table.coin_supplier.onyx) == 4
    assert len(my_game.game_table.coin_supplier.gold) == 5


def test_setup_cards(my_game: model.components.Game, my_users: List[database.user.User]):
    for user in my_users[:4]:
        controller.add_player(my_game, user)
    controller.game_setup.setup_cards(my_game)

    assert isinstance(my_game.game_table.card_supplier[1], model.components.CardSupplier)
    assert my_game.game_table.card_supplier[1].level == 1
    assert len(my_game.game_table.card_supplier[1].drawpile) == 40-4
    assert len(my_game.game_table.card_supplier[1].revealed) == 4

    assert isinstance(my_game.game_table.card_supplier[2], model.components.CardSupplier)
    assert my_game.game_table.card_supplier[2].level == 2
    assert len(my_game.game_table.card_supplier[2].drawpile) == 30-4
    assert len(my_game.game_table.card_supplier[2].revealed) == 4

    assert isinstance(my_game.game_table.card_supplier[3], model.components.CardSupplier)
    assert my_game.game_table.card_supplier[3].level == 3
    assert len(my_game.game_table.card_supplier[3].drawpile) == 20-4
    assert len(my_game.game_table.card_supplier[3].revealed) == 4


def test_setup_tiles(my_game: model.components.Game, my_users: List[database.user.User]):
    for user in my_users[:4]:
        controller.add_player(my_game, user)
    controller.game_setup.setup_tiles(my_game)
    assert len(my_game.game_table.tile_supplier) == 5
