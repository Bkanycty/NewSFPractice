import React from "react";
import { Link } from "react-router-dom";

const Calculator = () => {
    return(
        <>
            <nav>
                <Link to="/">Главная страница</Link>
            </nav>
            <div>
                <h1>Здесь будет калькулятор</h1>
            </div>
        </>
    );
}

export default Calculator;