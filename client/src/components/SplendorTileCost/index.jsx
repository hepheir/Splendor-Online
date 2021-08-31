import classNames from "classnames";
import React from "react";

import SplendorNumber from "../SplendorNumber";
import SplendorGemMiniGem from "../SplendorGemMiniGem";

import "./style.css";

class SplendorTileCost extends React.Component {
    render() {
        const { gem_type, cost } = this.props;

        if (!cost) return null;

        return (
            <div
                className={classNames("spl_noble-cost", this.props.className)}
                data-gem-type={gem_type}
            >
                <SplendorGemMiniGem className="spl_noble-cost_mini-gem" gem_type={gem_type}></SplendorGemMiniGem>
                <SplendorNumber className="spl_noble-cost_number">{cost}</SplendorNumber>
            </div>
        );
    }
}

export default SplendorTileCost;
