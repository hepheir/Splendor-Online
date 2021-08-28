import classNames from "classnames";
import React from "react";

import "./style.css";

import SplendorNumber from "../SplendorNumber";
import SplendorMiniGem from "../SplendorMiniGem";

class SplendorCardCost extends React.Component {
    render() {
        const { gem_type, cost } = this.props;

        if (!cost) return null;

        return (
            <div
                className={classNames("spl_card-cost", this.props.className)}
                data-gem-type={gem_type}
            >
                <SplendorMiniGem gem_type={gem_type}></SplendorMiniGem>
                <SplendorNumber>{cost}</SplendorNumber>
            </div>
        );
    }
}

export default SplendorCardCost;
