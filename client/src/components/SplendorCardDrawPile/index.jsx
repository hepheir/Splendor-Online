import React from "react";

import SplendorCard from "../SplendorCard";

import "./style.css";

class SplendorCardDrawPile extends React.Component {
    render() {
        const { level, className } = this.props;
        const _ILLUSTRATION = `hidden.lv${level}`;
        return (
            <SplendorCard
                className={className}
                illustration={_ILLUSTRATION}
            />
        );
    }
}

export default SplendorCardDrawPile;
