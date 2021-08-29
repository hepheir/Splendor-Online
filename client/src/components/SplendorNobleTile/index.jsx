import classNames from "classnames";
import React from "react";

import "./style.css";

import SplendorNumber from "../SplendorNumber";
import SplendorTileCost from "../SplendorTileCost";

const DEBUG_TILE_DATA = {
    id: 1,
    illustration: "noble.isabel_of_castille",
    prestige_point: 3,
    cost: {
        diamond: 4,
        sapphire: 0,
        emerald: 0,
        ruby: 0,
        onyx: 4,
    },
};


class SplendorNobleTile extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            tile: DEBUG_TILE_DATA,
            loaded: false,
        };
    }

    render() {
        const { tile } = this.state;
        return (
            <div
                className={classNames("spl_noble-tile", this.props.className)}
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

export default SplendorNobleTile;
