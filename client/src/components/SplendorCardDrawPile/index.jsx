import React from "react";

import SplendorCard from "../SplendorCard";

import "./style.css";

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
