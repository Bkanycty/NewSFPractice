import React from "react";

import "../styles/App.css";
import Header from "./header";
import Main from "./main";

function App() {
    const buttonName = "Some button";
    return (
        <>
            <Header buttonName={buttonName} />
            <Main />
        </>
        );
}


export default App;