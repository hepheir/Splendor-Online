import classNames from "classnames";
import React from "react";

import "./style.css";

class SplendorGem extends React.Component {
    render() {
        return (
            <div
                className={classNames("spl_gem", this.props.className)}
                style={this.props.style}
                data-gem-type={this.props.gem_type}
            ></div>
        );
    }
}

export default SplendorGem;
