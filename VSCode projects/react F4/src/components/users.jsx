import React from "react";
import { useLocation } from "react-router-dom";

function Users() {
    // Текущий адрес, где мы находимся в адресной строке
    const location = useLocation();
    // Получаем доступ к части после вопроса, где пишутся query параметры
    const search = location.search;
    // Объявляем query параметры
    const query = new URLSearchParams(search);
    
    return (
        <>
            <h2>
                {location.search}
                <br></br>
                Users with sorting: {query.get('sorting')} and filtering: {query.get('filtering')}
            </h2>
        </>
    );
}

export default Users;