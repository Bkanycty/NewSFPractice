import React, { useState } from "react";
import { Link, useParams } from "react-router-dom";
import Header from "./header";

export default function Category() {
    const params = useParams();
    const [cat, setCategory] = useState(undefined);
    const [recipeLinks, setRecipeLinks] = useState([]);
    const [recipeObjects, setRecipeObjects] = useState([]);

    if(!cat) {
        fetch("http://127.0.0.1:8000/categories/"+params.categoryId+"/")
        .then(response => response.json())
        .then(data => {
            setCategory(data);

            let recs = data.categoryRecipe
            setRecipeLinks(recs);
            
            recs.forEach(function(item) {
                fetch(item)
                .then(response => response.json())
                .then(data => {
                    setRecipeObjects(recipeObjects => [...recipeObjects, {id: data.id, name: data.name, cooking: data.cooking}]);
                })
            });
        })
        
        .catch(console.error())
    };

    return (
        <>
            <Header />
                {recipeObjects.map(recipe => 
                <>
                    <Link to={"/recipe/" + recipe.id} name={recipe.name} cooking={recipe.cooking}><br></br><h1>{recipe.name}</h1></Link>
                    <br></br>
                    <hr></hr>
                </>
                    )}
        </>
    )
}