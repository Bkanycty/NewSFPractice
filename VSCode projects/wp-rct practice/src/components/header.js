import React from "react";
import "../styles/header.css";
import { Link } from "react-router-dom";

function Header() {
    let btn1 = "Кнопка один"
    let btn2 = "Кнопка два"
    let btnLogout = "Log-out"
    return (
        <>
            <header>
                <button className="header-logo" onClick={() => console.log(window.innerWidth)}>Худеть - легко :)</button>
                <div className="header-navbar">
                    <Link to="/calculator" className="header-navbar-button">Calculator</Link>
                    <a href="http://localhost:8080/" className="header-navbar-button" onClick={() => console.log("Клик по кнопке " + btn2)}>{btn2}</a>
                </div>
                <div className="header-navbar header-logout">
                    <a href="http://localhost:8080/" className="header-navbar-button header-logout-button" onClick={() => console.log("Клик по кнопке " + btnLogout)}>{btnLogout}</a>
                </div>
            </header>
        </>
        );
}


export default Header;