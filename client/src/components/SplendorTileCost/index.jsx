import classNames from "classnames";
import React from "react";

import "./style.css";

import SplendorNumber from "../SplendorNumber";
import SplendorMiniGem from "../SplendorMiniGem";

class SplendorTileCost extends React.Component {
    render() {
        const { gem_type, cost } = this.props;

        if (!cost) return null;

        return (
            <div
                className={classNames("spl_noble-cost", this.props.className)}
                data-gem-type={gem_type}
            >
                <SplendorMiniGem className="spl_noble-cost_mini-gem" gem_type={gem_type}></SplendorMiniGem>
                <SplendorNumber className="spl_noble-cost_number">{cost}</SplendorNumber>
            </div>
        );
    }
}

export default SplendorTileCost;
