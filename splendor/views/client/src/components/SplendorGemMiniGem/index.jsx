import classNames from "classnames";
import React from "react";

import "./style.css";

class SplendorGemMiniGem extends React.Component {
    render() {
        const { gem_type, className } = this.props;

        return (
            <div
                className={classNames("spl_mini-gem", className)}
                data-gem-type={gem_type}
            />
        );
    }
}

export default SplendorGemMiniGem;
