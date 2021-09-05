from typing import Dict

from splendor import controller
from splendor import model


INTERMEDIARY = model.components.CoinContainer()

def _pre_gain_coins(game: model.components.Game) -> None:
    pass


def _post_gain_coins(game: model.components.Game) -> None:
    player = controller.game_util.current_player(game)
    while sum(player.player_coins) > 10:
        pass


def gain_coins(game: model.components.Game,
               coins: Dict[model.components.COIN_TYPE, int] = {}) -> None:
    # TODO: Check whether [2 same coins] or [3 diffrent coins] or [1, 2 diffrent coins (extremely depleted)]
    # TODO: Check whether piles are depleted
    # TODO: Coin transaction: table -> player
    # TODO: Check whether player has 10+ coins -> player should return the exceeds
    # TODO: Coin transaction: player -> table
    player = controller.game_util.current_player(game)

    # 코인을 3개보다 많이 가져가는 경우
    if sum(coins.values()) > 3:
        raise model.components.ErrorPlay('You cannot take coins more than 3.')

    # 코인을 3개 가져가는 경우에는, 서로다른 코인을 1개씩만 가져가야 함
    elif sum(coins.values()) == 3:
        if len(coins) < 3:
            raise model.components.ErrorPlay('You are taking 2 and 1 diffrent type of coins.')

    # 코인을 2개 가져가는 경우에는
    # 1. 같은 종류의 코인 2개를 가져가거나
    # 2. 서로다른 종류의 코인을 1씩 가져가되, 그 외의 모든 코인 공급처가 비어있어야 함.
    elif sum(coins.values()) == 2:
        if len(coins) < 2:
            selected_coin_type = coins[0]
            selected_coins_on_table = len(game.game_table.coin_supplier[selected_coin_type])

            sum()
            pass
    else:
        pass

    src = game.game_table.coin_supplier
    dst = player.player_coins

    try:
        for coin_type, amount in coins.items():
            src.send(INTERMEDIARY, coin_type, amount)
        INTERMEDIARY.send_all(dst)
        controller.game_util.log(game, f'    {player.user.user_name} gains '+', '.join(
            [f'{amount} {coin_type.name.lower()}' for coin_type, amount in coins.items()])+'.')
        controller.game_flow.end_turn(game)
    except:
        controller.game_util.log(game, '    Not enough coins to take.')
        INTERMEDIARY.send_all(src)


def action_buy_a_card(card: model.components.Card,
                      pay_diamond: int = 0,
                      pay_sapphire: int = 0,
                      pay_emerald: int = 0,
                      pay_ruby: int = 0,
                      pay_onyx: int = 0,
                      pay_gold: int = 0) -> None:
    # TODO: Calculate discounted card cost
    # TODO: Check whether the card is obtainable
    # TODO: Check where the card is (on deck, on hand)
    # TODO: Decide payment method
    # TODO: Coin transaction: player -> table
    # TODO: Card transaction: ??? -> player
    pass


def action_reserve_a_card(card: model.components.Card) -> None:
    # TODO: Check whether player can reserve more cards (max 3)
    # TODO: Check where the card is (on deck, on drawpile)
    # TODO: Card transaction: ??? -> player
    # TODO: Check whether gold coin is obtainable
    # TODO:   Coin transaction: table -> player
    pass
