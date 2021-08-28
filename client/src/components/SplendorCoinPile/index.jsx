import React from "react";

import "./style.css";

class SplendorCoinPile extends React.Component {
    render() {
        const { gem_type, count } = this.props;
        const stack = [];

        for (let i = 0; i < count; i++) {
            const unique_key = `spl_coin-pile_${gem_type}_${i}`;
            stack.push(<div className="spl_coin-pile" key={unique_key} />);
        }

        return (
            <div className="spl_coin-pile_container" data-gem-type={gem_type}>
                {stack}
            </div>
        );
    }
}

export default SplendorCoinPile;
