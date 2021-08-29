import classNames from "classnames";
import React from "react";

import "./style.css";

import SplendorCoin from "../SplendorCoin";

class SplendorCoinPile extends React.Component {
    render() {
        const { gem_type, count, className } = this.props;
        const stack = [];

        for (let i = 0; i < count; i++) {
            const unique_key = `spl_coin-pile_${gem_type}_${i}`;
            stack.push(<SplendorCoin className="spl_coin-pile_coin" gem_type={gem_type} key={unique_key} />);
        }

        return (
            <div className={classNames("spl_coin-pile", className)}>
                {stack}
            </div>
        );
    }
}

export default SplendorCoinPile;
