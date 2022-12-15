import * as React from "react";
import "../styles/Alerts.css"


function Alerts(props) {
    return (
        <>
            {
                React.Children.count(props.children)
            }
            { 
                React.Children.map(props.children, (child, index) => {
                    if(index < 2 ) {
                        return child;
                    }
                }) 
            }  
        </>
      );
}

export default Alerts;
