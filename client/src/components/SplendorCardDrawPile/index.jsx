import React from "react";

import SplendorCard from "../SplendorCard";

import "./style.css";

class SplendorCardDrawPile extends React.Component {
    render() {
        const { level, children, className } = this.props;
        const _ILLUSTRATION = `hidden.lv${level}`;
        return (
            <SplendorCard
                className={className}
                illustration={_ILLUSTRATION}
            >
                {children}
            </SplendorCard>
        );
    }
}

export default SplendorCardDrawPile;
