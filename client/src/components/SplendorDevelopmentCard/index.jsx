import classNames from "classnames";
import React from "react";

import "./style.css";

import SplendorCard from "../SplendorCard";
import SplendorCardCost from "../SplendorCardCost";
import SplendorGem from "../SplendorGem";
import SplendorNumber from "../SplendorNumber";

const DEBUG_CARD_DATA = {
    id: 1,
    level: 1,
    gem_bonus: "onyx",
    illustration: "onyx.mine",
    prestige_point: 3,
    cost: {
        diamond: 5,
        sapphire: 0,
        emerald: 1,
        ruby: 3,
        onyx: 1,
    },
};

class SplendorDevelopmentCard extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            card: DEBUG_CARD_DATA,
            face_up: true,
            loaded: false,
        };
    }

    render() {
        const { card } = this.state;
        return (
            <SplendorCard
                id={card.id}
                className={this.props.className}
                illustration={card.illustration}
            >
                <div className="spl_dev-card_header">
                    <SplendorNumber>{card.prestige_point}</SplendorNumber>
                    <SplendorGem
                        className="spl_dev-card_header_gem"
                        gem_type={card.gem_bonus}
                    />
                </div>
                <div className="spl_card-costs">
                    {Object.keys(card.cost).map((gem_type) => {
                        const unique_key = `card_${card.card_id}_${gem_type}`;
                        const cost = card.cost[gem_type];

                        if (!cost) return null;

                        return (
                            <SplendorCardCost
                                gem_type={gem_type}
                                cost={cost}
                                key={unique_key}
                            />
                        );
                    })}
                </div>
            </SplendorCard>
        );
    }
}

export default SplendorDevelopmentCard;
