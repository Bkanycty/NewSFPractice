import React from "react";
import { Link } from "react-router-dom";
import Header from "./header";
import "../styles/calculator.css";

const Calculator = () => {
    return(
        <>
            <Header />
            <div>
                <form className="calc-form" id="form-id">
                    Ваш пол: 
                    <input type="radio" id="male" name="gender" value="male"></input>
                    <label htmlFor="male">male</label>
                    <input type="radio" id="female" name="gender" value="female"></input>
                    <label htmlFor="female">female</label><br></br>

                    <label htmlFor="weight">Вес: </label>
                    <input type="number" min="40" max="300" title="Вес" id="weight"></input><br></br>

                    <label htmlFor="height">Рост, см: </label>
                    <input type="number" min="40" max="250" title="Рост" id="height"></input><br></br>

                    <label htmlFor="age">Полных лет: </label>
                    <input type="number" min="18" max="120" title="Возраст" id="age"></input><br></br>

                    <select size="1" multiple name="load-type" id="load-type-menu">
                        <option id="base" value="1" onClick={() => {
                            (document.getElementById("load-type-menu").size == "1" ?
                            document.getElementById("load-type-menu").size = "8" :
                            document.getElementById("load-type-menu").size = "1")
                            }}>Выберите тип нагрузок: </option>
                        <option id="a" value="1.2" onClick={() => {
                            document.getElementById("load-type-menu").size = "1";
                            document.getElementById("a").setAttribute("selected", "true");
                            document.getElementById("base").innerHTML = "Минимальные нагрузки (сидячая работа)";
                            document.getElementById("base").setAttribute("value", "1.2");
                            }}>Минимальные нагрузки (сидячая работа)</option>
                        <option id="b" value="1.375" onClick={() => {
                            document.getElementById("load-type-menu").size = "1";
                            document.getElementById("b").setAttribute("selected", "true");
                            document.getElementById("base").innerHTML = "Необременительные тренировки 3 раза в неделю";
                            document.getElementById("base").setAttribute("value", "1.375");
                            }}>Необременительные тренировки 3 раза в неделю</option>
                        <option id="c" value="1.4625" onClick={() => {document.getElementById("load-type-menu").size = "1"}}>Тренировки 5 раз в неделю (работа средней тяжести)</option>
                        <option id="d" value="1.550" onClick={() => {document.getElementById("load-type-menu").size = "1"}}>Интенсивные тренировки 5 раз в неделю</option>
                        <option id="e" value="1.6375" onClick={() => {document.getElementById("load-type-menu").size = "1"}}>Ежедневные тренировки</option>
                        <option id="f" value="1.725" onClick={() => {document.getElementById("load-type-menu").size = "1"}}>Ежедневные интенсивные тренировки или занятия 2 раза в день</option>
                        <option id="g" value="1.9" onClick={() => {document.getElementById("load-type-menu").size = "1"}}>Тяжелая физическая работа или интенсивные тренировки 2 раза в день</option>
                    </select><br></br>
                    <button type="button" formNoValidate form="form-id" onClick={() => {
                        const form = document.getElementById("form-id");
                        console.log(form.elements["gender"].value);
                        console.log(form.elements["weight"].value);
                        // ПРОДОЛЖИТЬ ЗДЕСЬ
                    }}>Рассчитать</button>
                </form>
                <div className="results">
                    Для похудения вам нужно потреблять не более: <br></br>
                    Для поддержания веса вам нужно потреблять: <br></br>
                    Для набора веса вам нужно потреблять не менее: <br></br>
                </div>
            </div>
        </>
    );
}

export default Calculator;