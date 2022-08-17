const temperature = Number(prompt('Введите температуру по Цельсию'))
if (isNaN(temperature) === false) {
    console.log(`${temperature} градусов по Цельсию равны ${((temperature * 9/5) + 32)} градусам по Фаренгейту`)
} else {
    console.log('Введите числовое значение')
}
