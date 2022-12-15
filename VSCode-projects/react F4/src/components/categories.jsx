import React, { useState } from "react";
import { Link, useParams, useLocation } from "react-router-dom";
import Header from "./header";
import axios from "axios";
import "../styles/categories.css"

export default function Categories() {
    const location = useLocation();
    const params = useParams();
    const [cats, setCats] = useState([]);
    if(!cats.length) {
        axios.get("http://127.0.0.1:8000/categories/").then(res => {
            setCats(res.data);
        });
    }
    return (
        <>
            <Header />
            <p><h1>Категории:</h1></p>
            {cats.map(category => 
            <>
                <p><h1><Link to={location.pathname+"category/"+category.id} key={category.name}>{category.name}</Link></h1></p>
                <hr></hr>
        </>)}
        </>
    );
}
