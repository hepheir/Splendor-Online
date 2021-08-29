import React from "react";

import "./style.css";

import SplendorCard from "../SplendorCard";

class SplendorCardDrawPile extends React.Component {
    render() {
        const { level } = this.props;
        const illustration_id = `drawpile.lv${level}`;
        return (
            <SplendorCard
                className={this.props.className}
                illustration={illustration_id}
            />
        );
    }
}

export default SplendorCardDrawPile;
