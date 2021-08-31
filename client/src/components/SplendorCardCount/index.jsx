import classNames from "classnames";
import React from "react";

import SplendorNumber from "../SplendorNumber";

import "./style.css";

class SplendorCardCount extends React.Component {
    render() {
        const { gem_type, count } = this.props;
        return (
            <div
                className={classNames("spl_card-count", this.props.className)}
                data-gem-type={gem_type}
            >
                <SplendorNumber className="spl_card-count_number">{count}</SplendorNumber>
            </div>
        );
    }
}

export default SplendorCardCount;
