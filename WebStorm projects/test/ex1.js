const ask = prompt('Введите ваши имя и фамилию')
var response = ask.split(" ")
if (response.length === 2 & typeof(response[0]) === "string" & typeof(response[1]) === "string") {
    alert(`Привет, ${response[0]} ${response[1]}`)
} else {
    console.log('Что-то пошло не так')
}

