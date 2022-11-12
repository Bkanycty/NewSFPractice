import React from "react";
import ReactDOM from "react-dom";

// import App from "./components/App";
import ReduxApp from "../App-redux";
import { Provider } from "react-redux";
import { createStore, applyMiddleware, compose } from "redux";
import reducer from "./redux/reducers"
import { logging } from "./middlewares/logging";

const store = createStore(reducer, 
    compose(
        applyMiddleware(logging), 
        window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()));
    


// const testButton = document.querySelector(".testButton")
// const items = document.querySelector(".testUl")
// const inputValue = document.querySelector(".testInput")

// store.subscribe(() => {
//     items.innerHTML = ""
//     inputValue.value = ""

//     store.getState().map(item => {
//         const li = document.createElement("li");
//         li.textContent = item;
//         items.appendChild(li)
//     })
// })

// testButton.addEventListener("click", ()=>{
//     console.log("INPUT", inputValue.value)
//     store.dispatch({type: "WRITE", payload: inputValue.value})
// })

// ReactDOM.render(<App/>, document.getElementById("root"));
ReactDOM.render(
    <Provider store={store}>
        <ReduxApp />
    </Provider>,
    document.getElementById("root"));
