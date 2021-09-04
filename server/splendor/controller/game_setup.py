from random import shuffle

from splendor.controller.game_util import cast_card, cast_tile
from splendor.database.user import User
from splendor.database.splendor_card import get_all_cards_by_level
from splendor.database.splendor_tile import get_random_tiles
from splendor.model.components import COIN_TYPE, GAME_STATUS, CardSupplier, Coin, Game, Player


def create_new_game(game_id: str) -> Game:
    # TODO: Implement unique id per game
    return Game(game_id)


def add_player(game: Game, user: User) -> None:
    if game.game_status != GAME_STATUS.PRE_GAME:
        print('Players only can join before the game starts.')
        return

    for player in game.game_players:
        if player.user.user_id is user.user_id:
            print(f'{user.user_name} has already joined the game #{game.game_id}.')
            return

    print(f'{user.user_name} joined the game #{game.game_id}.')
    new_player = Player(user)
    game.game_players.append(new_player)


def setup_coins(game: Game) -> None:
    _N_WILD_COINS = 5
    _N_COINS_PER_GEM = 7

    # Remove three of each coins for two player games,
    if len(game.game_players) == 2:
        _N_COINS_PER_GEM -= 3
    # ...and two of each for three player games.
    elif len(game.game_players) == 3:
        _N_COINS_PER_GEM -= 2

    for coin_type in COIN_TYPE:
        n_coins = _N_COINS_PER_GEM
        if coin_type == COIN_TYPE.GOLD:
            n_coins = _N_WILD_COINS

        for i in range(n_coins):
            coin_id = f'coin.{coin_type.name.lower()}.{i}'
            coin = Coin(coin_id, coin_type, game.game_table.coin_supplier)
            game.game_coins[coin_id] = coin
            game.game_table.coin_supplier[coin_type].append(coin)


def setup_cards(game: Game) -> None:
    _N_CARDS_PER_LEVEL = 4

    # Setting cards
    for card_level in (1, 2, 3):
        game.game_table.card_supplier[card_level] = CardSupplier(card_level)
        for db_card in get_all_cards_by_level(card_level):
            card = cast_card(db_card)
            game.game_cards[card.card_id] = card
            game.game_table.card_supplier[card_level].drawpile.append(card)

        shuffle(game.game_table.card_supplier[card_level].drawpile)

        for i in range(_N_CARDS_PER_LEVEL):
            card = game.game_table.card_supplier[card_level].drawpile.pop()
            game.game_table.card_supplier[card_level].revealed.append(card)


def setup_tiles(game: Game) -> None:
    _N_TILES = len(game.game_players)+1

    # Setting tiles
    for db_tile in get_random_tiles(_N_TILES):
        tile = cast_tile(db_tile)
        game.game_tiles[tile.tile_id] = tile
        game.game_table.tile_supplier.append(tile)
