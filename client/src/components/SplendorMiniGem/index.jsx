import classNames from "classnames";
import React from "react";

import "./style.css";

class SplendorMiniGem extends React.Component {
    render() {
        if (!this.props.gem_type) {
            throw Error("You must pass valid gem_type.");
        }

        return (
            <div
                className={classNames("spl_mini-gem", this.props.className)}
                style={this.props.style}
                data-gem-type={this.props.gem_type}
            ></div>
        );
    }
}

export default SplendorMiniGem;
