import React from "react";
import "../styles/header.css";
import { Link } from "react-router-dom";

function Header() {
    return (
        <>
            <header>
                <Link to="/" className="header-logo">Рецепты от бабули :)</Link>
                <div className="header-navbar">
                    <Link to="/api" className="header-navbar-button">API</Link>
                    <Link to="/" className="header-navbar-button">Категории</Link>
                </div>
            </header>
        </>
        );
}


export default Header;