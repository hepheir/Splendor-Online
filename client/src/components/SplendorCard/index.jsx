import classNames from "classnames";
import React from "react";

import "./style.css";

class SplendorCard extends React.Component {
    render() {
        return (
            <div
                className={classNames("spl_card", this.props.className)}
                data-card-illustration={this.props.illustration}
            >
                {this.props.children}
            </div>
        );
    }
}

export default SplendorCard;
