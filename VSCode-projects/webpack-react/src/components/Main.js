import React, { Component } from "react";
import "../styles/Main.css"
import Countries from "./Countries";
import Alerts from "./Alerts";
import Alert from 'react-bootstrap/Alert';

function Main() {
    let alertText = "This is some text for alert!";
    return (
        <main>
            <Alerts>
                <Alert variant={"danger"}>{ alertText }</Alert>
                <Alert variant={"success"}>{ alertText }</Alert>
                <Alert variant={"warning"}>{ alertText }</Alert>
            </Alerts>
            <Countries />
        </main>
    );
}

export default Main;