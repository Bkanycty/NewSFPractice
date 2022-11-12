// Создаём состояние приложения
const state = [
    {
        id: 1,
        task: 'Do homework',
        completed: true,
    },
    {
        id: 2,
        task: 'Buy bread',
        completed: false,
    }
]

// Добавляем действие
const action = {
    type: 'ADD_TODO',
    task: 'Learn new words',
    id: 3,
}


// Пишем функцию-reducer
function reducer(currentState, action) {
    switch (action.type) {
        case 'ADD_TODO': {
            const newState = [
                ...currentState,
                {
                    id: action.id,
                    task: action.task,
                    completed: false
                }
            ]
            return newState
        }
        break;
        default:
            return currentState
    }
}