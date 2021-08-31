import classNames from "classnames";
import React from "react";

import SplendorNumber from "../SplendorNumber";

import "./style.css";

class SplendorCardCount extends React.Component {
    render() {
        const { gem_type, count, className } = this.props;
        const depleted_flag = (!count) ? 'spl_depleted' : null;
        return (
            <div
                className={classNames("spl_card-count", depleted_flag, className)}
                data-gem-type={gem_type}
            >
                <SplendorNumber className="spl_card-count_number">{count}</SplendorNumber>
            </div>
        );
    }
}

export default SplendorCardCount;
