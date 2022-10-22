import React, { useState } from "react";
import axios from "axios";


function Countries() {
    const [countries, setCountries] = useState([]);
    if(!countries.length) {
        axios.get("C:\text.html").then(res => {
            console.log(res);
            setCountries(res.data);
        });
    }
    return (
        <table>
            <thead><tr><th>Name</th><th>Capital</th></tr></thead>
            <tbody>
                {countries.map(country => <tr key={country.alpha3Code}>
                    <td>{country.name}</td>
                    <td>{country.capital}</td></tr>)}
            </tbody>
        </table>
    );
}

export default Countries;