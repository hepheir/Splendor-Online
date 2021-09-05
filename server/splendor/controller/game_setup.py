from random import shuffle

from splendor.controller import game_util
from splendor.database import splendor_card, splendor_tile
from splendor.model import components


def setup_coins(game: components.Game) -> None:
    _N_WILD_COINS = 5
    _N_COINS_PER_GEM = 7

    # Remove three of each coins for two player games,
    if len(game.game_players) == 2:
        _N_COINS_PER_GEM -= 3
    # ...and two of each for three player games.
    elif len(game.game_players) == 3:
        _N_COINS_PER_GEM -= 2

    for coin_type in components.COIN_TYPE:
        n_coins = _N_COINS_PER_GEM
        if coin_type == components.COIN_TYPE.GOLD:
            n_coins = _N_WILD_COINS

        for i in range(n_coins):
            coin_id = f'coin.{coin_type.name.lower()}.{i}'
            coin = components.Coin(coin_id, coin_type)
            game.game_table.coin_supplier[coin_type].append(coin)


def setup_cards(game: components.Game) -> None:
    _N_CARDS_PER_LEVEL = 4

    # Setting cards
    for card_level in (1, 2, 3):
        game.game_table.card_supplier[card_level] = components.CardSupplier(
            card_level)
        for db_card in splendor_card.get_all_cards_by_level(card_level):
            card = game_util.cast_card(db_card)
            game.game_table.card_supplier[card_level].drawpile.append(card)

        shuffle(game.game_table.card_supplier[card_level].drawpile)

        for i in range(_N_CARDS_PER_LEVEL):
            card = game.game_table.card_supplier[card_level].drawpile.pop()
            game.game_table.card_supplier[card_level].revealed.append(card)


def setup_tiles(game: components.Game) -> None:
    _N_TILES = len(game.game_players)+1

    # Setting tiles
    for db_tile in splendor_tile.get_random_tiles(_N_TILES):
        tile = game_util.cast_tile(db_tile)
        game.game_table.tile_supplier.append(tile)
