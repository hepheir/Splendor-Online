from dataclasses import asdict

from splendor.app import app
from splendor import database, controller



@app.get('/game_object/<asset_type>/<asset_id>')
def get_game_object(asset_type: str, asset_id: str):
    try:
        if asset_type == 'card':
            db_card = database.splendor_card.get_card_by_id(asset_id)
            card = controller.game_util.cast_card(db_card)
            data = asdict(card)
        if asset_type == 'tile':
            db_tile = database.splendor_tile.get_tile_by_id(asset_id)
            card = controller.game_util.cast_tile(db_tile)
            data = asdict(card)
        return {
            'error': None,
            'data': data
        }
    except Exception as exception:
        return {
            'error': exception.args,
            'data': None,
        }


@app.get('/user/<user_id>')
def get_user(user_id: int):
    try:
        user = database.user.get_user_by_id(user_id)
        data = asdict(user)
        return {
            'error': None,
            'data': data
        }
    except Exception as exception:
        return {
            'error': exception.args,
            'data': None,
        }
