import classNames from "classnames";
import React from "react";

import "./style.css";

class SplendorCoin extends React.Component {
    render() {
        const { gem_type, className } = this.props;

        return (
            <div className={classNames("spl_coin", className)} gem_type={gem_type} />
        );
    }
}

export default SplendorCoin;
