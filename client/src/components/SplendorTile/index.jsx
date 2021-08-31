import classNames from "classnames";
import React from "react";

import SplendorNumber from "../SplendorNumber";
import SplendorTileCost from "../SplendorTileCost";

import "./style.css";

import { api_get_asset_info } from "../../api";


class SplendorTile extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            tile: {
                id: null,
                illustration: null,
                prestige_point: null,
                cost: {
                    diamond: null,
                    emerald: null,
                    onyx: null,
                    ruby: null,
                    sapphire: null
                },
            },
        };
    }

    componentDidMount() {
        const { tile_id } = this.props;

        api_get_asset_info('tile', tile_id)
            .then(
                (result) => {
                    this.setState({
                        isLoaded: true,
                        tile: result.data,
                    })
                },
                (error) => {
                    this.setState({
                        isLoaded: true,
                        error
                    })
                }
            );
    }

    render() {
        const { className } = this.props;
        const { error, isLoaded, tile } = this.state;

        if (error) {
            return (
                <div className={classNames("spl_noble-tile", className)}>
                    Error: {error.message}
                </div>
            );
        }
        else if (!isLoaded) {
            return (
                <div className={classNames("spl_noble-tile", className)}>
                    Loading...
                </div>
            );
        }
        else {
            return (
                <div
                    className={classNames("spl_noble-tile", className)}
                    data-illustration={tile.illustration}
                >
                    <div className="spl_noble-tile_costs">
                        {Object.keys(tile.cost).map((gem_type) => {
                            const unique_key = `tile_${tile.card_id}_${gem_type}`;
                            const cost = tile.cost[gem_type];

                            if (!cost) return null;

                            return (
                                <SplendorTileCost
                                    gem_type={gem_type}
                                    cost={cost}
                                    key={unique_key}
                                />
                            );
                        })}
                    </div>
                    <SplendorNumber className="spl_noble-tile_prestige-point">
                        {tile.prestige_point}
                    </SplendorNumber>
                </div>
            );
        }
    }
}

export default SplendorTile;
