import React, { Fragment } from "react";

import "../styles/App.css";
import Header from "./header";
import Main from "./main";

function App() {
    const buttonName = "Some button updated 2";
    return (
        <Fragment>
            <Header buttonName={buttonName} />
            <Main />
        </Fragment>
        );
}


export default App;