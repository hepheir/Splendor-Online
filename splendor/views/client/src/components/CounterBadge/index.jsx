import classNames from "classnames";
import React from "react";

import "./style.css";

class CounterBadge extends React.Component {
    render() {
        const { count, className, style } = this.props;
        return (
            <div className={classNames("spl_counter-badge", className)} style={style}>
                {count}
            </div>
        );
    }
}

export default CounterBadge;
