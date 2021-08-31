import classNames from "classnames";
import React from "react";

import SplendorCard from "../SplendorCard";
import SplendorCardCost from "../SplendorCardCost";
import SplendorGem from "../SplendorGem";
import SplendorNumber from "../SplendorNumber";

import "./style.css";

import { api_get_asset_info } from "../../api";


class SplendorCardDevelopmentCard extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            card: {
                id: null,
                level: null,
                gem_bonus: null,
                illustration: null,
                prestige_point: null,
                cost: {
                    diamond: null,
                    sapphire: null,
                    emerald: null,
                    ruby: null,
                    onyx: null,
                },
            },
            is_face_up: true,
        };
    }

    componentDidMount() {
        const { card_id } = this.props;

        api_get_asset_info('card', card_id)
            .then(
                (result) => {
                    this.setState({
                        isLoaded: true,
                        card: result.data,
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
        const { error, isLoaded, card } = this.state;

        if (error) {
            return <div>Error: {error.message}</div>
        }
        else if (!isLoaded) {
            return (
                <SplendorCard className={classNames(className)}>
                    Loading...
                </SplendorCard>
            );
        }
        else {
            return (
                <SplendorCard
                    id={card.id}
                    className={classNames(className)}
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
}

export default SplendorCardDevelopmentCard;
