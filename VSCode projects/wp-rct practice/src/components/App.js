import React from "react";
import "../styles/App.css";
import Header from "./header";
import "../styles/header.css";
import Main from "./main";
import "../styles/main.css";
import Calculator from "./Calculator";
import { Route, Link, Routes } from "react-router-dom";

function App() {
    return (
        <div className="App">
            <Header />
            <Main />
        </div>
    );
}


export default App;