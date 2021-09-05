from typing import Dict

from splendor.controller import game_util, game_flow, game_setup, game_action
from splendor.database import user
from splendor.model import components


RUNNING_GAMES: Dict[components._T_ID, components.Game] = {}


def get_game_by_id(game_id:str) -> components.Game:
    if game_id not in RUNNING_GAMES:
        raise Exception(f"Couldn't find game with id {game_id}")
    return RUNNING_GAMES[game_id]


def create_new_game(game_id: str) -> components.Game:
    # TODO: Implement unique id per game
    game = components.Game(game_id)
    game.game_status = components.GAME_STATUS.PRE_GAME
    game_util.log(game, '')
    game_util.log(game, '[new game]')
    RUNNING_GAMES[game.game_id] = game
    return game


def add_player(game: components.Game, user: user.User) -> None:
    if game.game_status != components.GAME_STATUS.PRE_GAME:
        game_util.log(game, 'Players only can join before the game starts.')
        return

    for player in game.game_players:
        if player.user.user_id is user.user_id:
            game_util.log(game, f'{user.user_name} has already joined the game.')
            return

    game_util.log(game, f'{user.user_name} joined the game.')
    new_player = components.Player(user)
    game.game_players.append(new_player)
