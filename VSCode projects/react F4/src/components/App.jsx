import React from "react";
import "../styles/App.css";
import "../styles/header.css";
import Categories from "./categories.jsx";
import { Route, Routes, HashRouter } from "react-router-dom";
import Recipes from "./recipes.jsx";
import Category from "./category.jsx";
import SwaggerUI from "swagger-ui-react"
import "swagger-ui-react/swagger-ui.css"



function App() {
    return (
        <>
            <HashRouter>
                <Routes>
                    <Route path="/" element={<Categories />} />
                    <Route path="/category/:categoryId" element={<Category />} />
                    <Route path="recipe/:recipeId" element={<Recipes />} />
                    <Route path="/api" element={<SwaggerUI url="http://127.0.0.1:8000/openapi/" />} />
                </Routes>
            </HashRouter>
        </>
    );
}


export default App;