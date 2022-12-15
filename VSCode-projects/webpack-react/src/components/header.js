import React, { useState } from "react";
import "../styles/Header.css"



function Header(props) {
    let [count, setNewCount] = useState(0);
    const handleClick = () => {
        setNewCount(count + 1);
    }
    return (
        <header>This is header
            <button className={ "some-button" } onClick={handleClick}>
                {props.buttonName}, clicked:{count} times</button>
        </header>
    )
}

export default Header;