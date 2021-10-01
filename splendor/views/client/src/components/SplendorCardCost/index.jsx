import classNames from "classnames";
import React from "react";

import SplendorNumber from "../SplendorNumber";
import SplendorGemMiniGem from "../SplendorGemMiniGem";

import "./style.css";

class SplendorCardCost extends React.Component {
    render() {
        const { gem_type, cost } = this.props;

        if (!cost) return null;

        return (
            <div
                className={classNames("spl_card-cost", this.props.className)}
                data-gem-type={gem_type}
            >
                <SplendorGemMiniGem gem_type={gem_type}></SplendorGemMiniGem>
                <SplendorNumber>{cost}</SplendorNumber>
            </div>
        );
    }
}

export default SplendorCardCost;
