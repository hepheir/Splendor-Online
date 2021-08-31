import React from "react";

import SplendorCardCount from "../../components/SplendorCardCount";
import SplendorCardDevelopmentCard from "../../components/SplendorCardDevelopmentCard";
import SplendorCardDrawPile from "../../components/SplendorCardDrawPile";
import SplendorCoinCount from "../../components/SplendorCoinCount";
import SplendorCoinPile from "../../components/SplendorCoinPile";
import SplendorGemMiniGem from "../../components/SplendorGemMiniGem";
import SplendorTile from "../../components/SplendorTile";

import "./style.css";

const GEM_TYPES = ["diamond", "sapphire", "emerald", "ruby", "onyx", "gold"];

class InGame extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            playerId: 1,
            players: [
                {
                    id: 1,
                    name: "Hepheir",
                    prestige_points: 0,
                    hand: {
                        resources: {
                            diamond: { cards: 0, coins: 1 },
                            sapphire: { cards: 1, coins: 3 },
                            emerald: { cards: 5, coins: 0 },
                            ruby: { cards: 5, coins: 0 },
                            onyx: { cards: 5, coins: 2 },
                            gold: { coins: 0 },
                        },
                        reserves: [14],
                        tiles: [1, 3, 4, 5, 6],
                    },
                },
                {
                    id: 2,
                    name: "koreair",
                    prestige_points: 0,
                    hand: {
                        resources: {
                            diamond: { cards: 3, coins: 0 },
                            sapphire: { cards: 1, coins: 1 },
                            emerald: { cards: 0, coins: 0 },
                            ruby: { cards: 0, coins: 1 },
                            onyx: { cards: 1, coins: 1 },
                            gold: { coins: 3 },
                        },
                        reserves: [1,3],
                        tiles: [2],
                    },
                },
            ],
            table: {
                tiles: [1, 3, 5, 7, 9],
                cards: {
                    3: [72, 89, 76, 82],
                    2: [44, 64, 57, 50],
                    1: [18, 27, 5, 21],
                },
                coins: {
                    diamond: 5,
                    sapphire: 5,
                    emerald: 5,
                    ruby: 5,
                    onyx: 5,
                    gold: 5,
                },
            },
        };
        this.countCoinsInHand = this.countCoinsInHand.bind(this);

        this.renderPlayerBoards = this.renderPlayerBoards.bind(this);

        this.renderCardSupplier = this.renderCardSupplier.bind(this);
        this.renderCoinSupplier = this.renderCoinSupplier.bind(this);
        this.renderTileSupplier = this.renderTileSupplier.bind(this);
        this.renderHandGems = this.renderHandCounts.bind(this);
    }

    countCoinsInHand() {
        const { playerId, players } = this.state;
        const { hand } = players.find((player) => player.id === playerId);
        let count = 0;
        for (const gem_type in hand.resources) {
            count += hand.resources[gem_type].coins;
        }
        return count;
    }

    renderCardSupplier() {
        const { cards } = this.state.table;
        const _LEVEL_ORDER = [3, 2, 1];
        const f_card_container = (card_id) => {
            const _UNIQUE_KEY = `spl_card-supplier_card.${card_id}`;
            return (
                <div
                    className="spl_card-supplier_card-container"
                    key={_UNIQUE_KEY}
                >
                    {card_id ? (
                        <SplendorCardDevelopmentCard card_id={card_id} />
                    ) : null}
                </div>
            );
        };
        const f_card_supplier = (card_level) => {
            const _UNIQUE_KEY = `spl_card-supplier.${card_level}`;
            return (
                <div className="spl_card-supplier" key={_UNIQUE_KEY}>
                    <div className="spl_card-supplier_card-container">
                        <SplendorCardDrawPile level={card_level} />
                    </div>
                    {cards[card_level].map(f_card_container)}
                </div>
            );
        };
        return (
            <div className="spl_card-suppliers">
                {_LEVEL_ORDER.map(f_card_supplier)}
            </div>
        );
    }

    renderCoinSupplier() {
        const { coins } = this.state.table;
        const f_coin_pile = (gem_type) => {
            const _UNIQUE_KEY = `spl_coin-supplier_coin-pile.${gem_type}`;
            return (
                <SplendorCoinPile
                    className="spl_coin-supplier_coin-pile"
                    gem_type={gem_type}
                    count={coins[gem_type]}
                    key={_UNIQUE_KEY}
                />
            );
        };
        return (
            <div className="spl_coin-supplier">
                {GEM_TYPES.map(f_coin_pile)}
            </div>
        );
    }

    renderTileSupplier() {
        const { tiles } = this.state.table;
        const f_noble_tile = (tile_id) => {
            const _UNIQUE_KEY = `spl_tile-supplier_tile.${tile_id}`;
            return <SplendorTile tile_id={tile_id} key={_UNIQUE_KEY} />;
        };
        return (
            <div className="spl_tile-supplier horizontal">
                {tiles.map(f_noble_tile)}
            </div>
        );
    }

    renderHandCounts() {
        const { playerId, players } = this.state;
        const { hand } = players.find((player) => player.id === playerId);
        const f_resource = (gem_type) => {
            const _RESOURCE = hand.resources[gem_type];
            const _UNIQUE_KEY = `spl_hand_counts.${gem_type}`;
            return (
                <div
                    className="spl_hand_counts"
                    data-gem-type={gem_type}
                    key={_UNIQUE_KEY}
                >
                    {gem_type !== "gold" ? (
                        <>
                            <SplendorGemMiniGem
                                className="spl_hand_counts_mini-gem"
                                gem_type={gem_type}
                            />
                            <SplendorCardCount
                                className="spl_hand_counts_card-count"
                                gem_type={gem_type}
                                count={_RESOURCE.cards}
                            />
                        </>
                    ) : null}
                    <SplendorCoinCount
                        className="spl_hand_counts_coin-count"
                        gem_type={gem_type}
                        count={_RESOURCE.coins}
                    />
                </div>
            );
        };
        return (
            <div className="spl_hand_gems">
                <div className="spl_hand_gems_desc">
                    내 보석 ({this.countCoinsInHand()}/10)
                </div>
                {GEM_TYPES.map(f_resource)}
            </div>
        );
    }

    renderHandReservedCards() {
        return <div className="my-reserved-cards"></div>;
    }

    renderPlayerBoards() {
        const { players } = this.state;
        const f_player_resources = (player, gem_type) => {
            const { id, hand } = player;
            const { cards, coins } = hand.resources[gem_type];
            const _UNIQUE_KEY = `spl_player-board.${id}.resource.${gem_type}`;
            return (
                <div className="spl_player-board_resource" key={_UNIQUE_KEY}>
                    {gem_type !== "gold" ? (
                        <SplendorCardCount
                            className="spl_player-board_card-count"
                            gem_type={gem_type}
                            count={cards}
                        />
                    ) : null}
                    <SplendorCoinCount
                        className="spl_player-board_coin-count"
                        gem_type={gem_type}
                        count={coins}
                    />
                </div>
            );
        };
        const f_player_card = (player, card_id, index) => {
            const { id } = player;
            const _UNIQUE_KEY = `spl_player-board.${id}.reserved-card.${card_id}.${index}`;
            return (
                <SplendorCardDevelopmentCard
                    className="spl_player-board_reserved-card"
                    card_id={card_id}
                    key={_UNIQUE_KEY}
                />
            );
        };
        const f_player_tile = (player, tile_id, index) => {
            const { id } = player;
            const _UNIQUE_KEY = `spl_player-board.${id}.tile.${tile_id}`;
            return (
                <SplendorTile
                    className="spl_player-board_tile"
                    tile_id={tile_id}
                    key={_UNIQUE_KEY}
                />
            );
        };
        const f_player_board = (player) => {
            const { id, name, prestige_points, hand } = player;
            const { reserves, tiles } = hand;
            const _UNIQUE_KEY = `spl_player-board.${id}`;
            return (
                <div className="spl_player-board" key={_UNIQUE_KEY}>
                    <div className="spl_player-board_pname">{name}</div>
                    <div className="spl_player-board_score">
                        {prestige_points} PP
                    </div>
                    <div className="spl_player-board_resources">
                        {GEM_TYPES.map((gem_type) =>
                            f_player_resources(player, gem_type)
                        )}
                    </div>
                    <div className="spl_player-board_reserved-cards">
                        {reserves.map((card_id, index) =>
                            f_player_card(player, card_id, index)
                        )}
                    </div>
                    <div className="spl_player-board_tiles">
                        {tiles.map((tile_id) =>
                            f_player_tile(player, tile_id)
                        )}
                    </div>
                </div>
            );
        };
        return (
            <div className="spl_player-boards">
                {players.map(f_player_board)}
            </div>
        );
    }

    render() {
        return (
            <>
                <aside id="player_boards" className="side-bar left">
                    {this.renderPlayerBoards()}
                </aside>
                <main id="main_board" className="main-board">
                    <div className="spl_table">
                        {this.renderCardSupplier()}
                        {this.renderCoinSupplier()}
                        {this.renderTileSupplier()}

                        {/* My Hand */}
                        <div className="spl_hand">
                            {this.renderHandCounts()}
                            <div className="my-reserved-cards"></div>
                            <div className="my-noble-tiles"></div>
                        </div>
                    </div>
                </main>
                <aside id="logs" className="side-bar right">
                    {/* <Logs /> */}
                </aside>
            </>
        );
    }
}

export default InGame;
