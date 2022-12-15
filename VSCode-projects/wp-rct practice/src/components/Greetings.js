import React from "react";

import "../styles/greetings.css";

function Greetings() {
    return (
        <>
            <div className="greetings greet">
                Вы здесь потому что испытываете желание похудеть. Что ж, поздравляю! Вы уже на четверть приблизились к своей мечте :)
                <p>Осталось выполнить всего 3 простых шага:</p>
            </div>
            <div className="greetings step step-1">
                Определить, сколько калорий в день необходимо вашему организму для поддержания веса и вычесть 25%
            </div>
            <div className="greetings step step-2">
                Составить меню на оставшееся после вычета количество калорий на день/два/три или больше в зависимости от того, насколько разнообразно вы привыкли питаться
            </div>
            <div className="greetings step step-3">
                Придерживаться
            </div>
        </>
        );
}


export default Greetings;