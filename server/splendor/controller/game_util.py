from io import TextIOWrapper
from os import path
from typing import Any, Dict

from splendor.database.splendor_card import SplendorCard
from splendor.database.splendor_tile import SplendorTile
from splendor.model.components import Card, Cost, Tile, Game, Player


_RUNNING_GAMES: Dict[Any, TextIOWrapper] = {}


def log(game: Game, *args, sep=' ', end='\n') -> None:
    if game.game_id not in _RUNNING_GAMES:
        file_name = path.join('splendor', 'log', f'{game.game_id}.log')
        _RUNNING_GAMES[game.game_id] = open(file_name, 'w')

    _RUNNING_GAMES[game.game_id].write(sep.join(map(str, args))+end)


def round(game: Game) -> int:
    return game.game_turn_number // len(game.game_players)


def current_player(game: Game) -> Player:
    return game.game_players[game.game_turn_number % len(game.game_players)]


def current_player_name(game: Game) -> str:
    return current_player(game).user.user_name


def cast_card(db_card: SplendorCard) -> Card:
    return Card(
        card_id=db_card.card_id,
        card_level=db_card.card_level,
        card_score=db_card.card_score,
        card_bonus=db_card.card_bonus,
        card_illustration=db_card.card_illustration,
        card_cost=Cost(diamond=db_card.card_cost_diamond,
                       sapphire=db_card.card_cost_sapphire,
                       emerald=db_card.card_cost_emerald,
                       ruby=db_card.card_cost_ruby,
                       onyx=db_card.card_cost_onyx))


def cast_tile(db_tile: SplendorTile) -> Tile:
    return Tile(tile_id=db_tile.tile_id,
                tile_score=db_tile.tile_score,
                tile_illustration=db_tile.tile_illustration,
                tile_cost=Cost(diamond=db_tile.tile_cost_diamond,
                               sapphire=db_tile.tile_cost_sapphire,
                               emerald=db_tile.tile_cost_emerald,
                               ruby=db_tile.tile_cost_ruby,
                               onyx=db_tile.tile_cost_onyx))
