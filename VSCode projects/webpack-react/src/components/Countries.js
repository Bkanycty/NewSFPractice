import React, { useState } from "react";
import axios from "axios";
import Table from "react-bootstrap/Table";
import 'bootstrap/dist/css/bootstrap.min.css';
import "../styles/Countries.css";
import Country from "./Country";

function Countries() {
    const [countries, setCountries] = useState([]);
    if(!countries.length) {
        axios.get("http://localhost:3000/countries").then(res => {
            console.log(res);
            setCountries(res.data);
        });
    }
    return (
        <Table striped bordered hover className="countries">
            <thead><tr><th>Name</th><th>Capital</th></tr></thead>
            <tbody>
                {countries.map(country => country.capital ? 
                <Country key={country.alpha3Code} name={country.name} capital={country.capital} /> :
                <Country key={country.alpha3Code} name={country.name} />)}
            </tbody>
        </Table>
    );
}

export default Countries;