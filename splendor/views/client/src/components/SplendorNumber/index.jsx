import classNames from "classnames";
import React from "react";

import "./style.css";

class SplendorNumber extends React.Component {
    render() {
        var number = this.props.children || 0;

        number = Number(number);
        number = Math.min(number, 10);
        number = Math.max(number, 0);

        return (
            <div
                className={classNames("spl_number", this.props.className)}
                data-number={number}
            ></div>
        );
    }
}

export default SplendorNumber;
