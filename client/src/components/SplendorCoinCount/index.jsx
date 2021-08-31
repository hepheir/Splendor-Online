import classNames from "classnames";
import React from "react";

import SplendorNumber from "../SplendorNumber";
import SplendorCoin from "../SplendorCoin";

import "./style.css";

class SplendorCoinCount extends React.Component {
    render() {
        const { gem_type, count, className } = this.props;
        return (
            <div className={classNames("spl_coin-count", className)}>
                <SplendorNumber className="spl_coin-count_number">{count}</SplendorNumber>
                <SplendorCoin
                    className="spl_hand_counts_coin-count_coin"
                    gem_type={gem_type}
                />
            </div>
        );
    }
}

export default SplendorCoinCount;
