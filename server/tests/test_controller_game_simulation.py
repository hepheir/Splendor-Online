import json
from dataclasses import asdict

from splendor import controller, database


game = controller.create_new_game("test.game_simulation")


def test_setting_up():
    controller.add_player(game, database.user.get_user_by_id(1))
    controller.add_player(game, database.user.get_user_by_id(2))
    controller.add_player(game, database.user.get_user_by_id(3))


def test_start_game():
    controller.game_flow.start_game(game)


def test_turn_1():
    # controller.game_util.log(game, json.dumps(asdict(game.game_table.card_supplier)))
    pass
