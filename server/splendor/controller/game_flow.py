from random import shuffle
from splendor import controller

from splendor import socketio
from splendor.controller import game_setup, game_util
from splendor.controller.game_action import INTERMEDIARY
from splendor.model.components import GAME_STATUS, Game


from splendor.database import crud

def game_setup():
    pass


def start_game(game: Game) -> None:
    if game.game_status != GAME_STATUS.PRE_GAME:
        game_util.log(game, 'The game has already been started.')
        return
    elif len(game.game_players) < 2:
        game_util.log(game, 'Not enough players to start game.')
        return
    else:
        game.game_status = GAME_STATUS.START_GAME
        game_util.log(game, '[setting game]')
        game.game_turn_number = 0
        shuffle(game.game_players)
        game_setup.setup_cards(game)
        game_setup.setup_coins(game)
        game_setup.setup_tiles(game)
        game_util.log(game, '[start game]')
        begin_round(game)
        return


def begin_round(game: Game) -> None:
    game.game_status = GAME_STATUS.BEGIN_ROUND
    game_util.log(game, f"Begin of the round #{game_util.round(game)}")
    begin_turn(game)


def end_round(game: Game) -> None:
    game.game_status = GAME_STATUS.END_ROUND
    game_util.log(game, f"End of the round #{game_util.round(game)}")
    if game.flag_last_round:
        game.end()
    else:
        game.begin_round()


def begin_turn(game: Game) -> None:
    game.game_status = GAME_STATUS.BEGIN_TURN
    game_util.log(game, f"  {game_util.current_player_name(game)}'s turn.")
    player = game_util.current_player(game)
    # TODO: Increase turn counter
    # TODO: Reset flags
    game.game_status = GAME_STATUS.WAITING_FOR_PRE_ACTION
    # game.turn.taken_coins.clear()
    # game.turn.paid_coins.clear()


def end_turn(game: Game) -> None:
    game.game_status = GAME_STATUS.END_TURN
    # TODO: Check for eligible Noble Tiles
    # TODO: Check player's score (game-end condition)
    # TODO: Restock card rows
    game.game_turn_number += 1
    if game.game_turn_number % len(game.game_players) == 0:
        end_round(game)
    else:
        begin_turn(game)
