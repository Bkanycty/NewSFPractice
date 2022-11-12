import React, { useState } from "react";
import { useParams } from "react-router-dom";
import Header from "./header";

export default function Recipes(props) {
    const params = useParams();
    let [cooking, setCooking] = useState([])
    if(!cooking.length) {fetch("http://127.0.0.1:8000/recipes/" + params.recipeId + "/").then(response => response.json())
        .then(data => {
        setCooking(cooking => [...cooking, data]);
        });
    }
    console.log(cooking)
    return (
        <>
            <Header />
            <div>
               {cooking.map(recipe => 
                    <>
                        <h1>{recipe.name}</h1>
                        <hr></hr>
                        <h3>{recipe.cooking}</h3>
                    </>
                        )}
            </div>
        </>
    )
}