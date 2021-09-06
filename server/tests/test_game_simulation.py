# Use `pytest -v -s` to see detailed workflow.

import pytest

from splendor import database, model


@pytest.fixture
def create_2_player_game():
    print()
    print("========================================================")
    print("[TEST]: Creating 2 players game.")
    print("--------------------------------------------------------")

    database.setup_sample_data()
    player_1 = model.User('player_1_host')
    player_2 = model.User('player_2')
    game = model.Game(player_1)
    game.join(player_2)

    print("--------------------------------------------------------")
    print("[TEST]: Start testing...")
    print("========================================================")
    print()

    yield (game, player_1, player_2)

    print()
    print("========================================================")
    print("[TEST]: End testing.")

    del player_1
    del player_2
    del game

    print("[TEST]: Teardown completed.")
    print("========================================================")
    print()


def test_2_player_game(create_2_player_game):
    game: model.Game
    p1: model.User
    p2: model.User

    game, p1, p2 = create_2_player_game

    game.start_game()

    if p1.db_row['user_id'] != game.player_db_rows[0]['user_id']:
        p1, p2 = p2, p1

    game.action(p2, 'gain_coin', diamond=1, sapphire=1, ruby=1)
    game.action(p1, 'gain_coin', diamond=1, sapphire=1, ruby=1, onyx=1)
