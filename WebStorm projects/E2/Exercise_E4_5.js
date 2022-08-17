// Задание 4.
//
//     Определить иерархию электроприборов. Включить некоторые в розетку. Посчитать потребляемую мощность.
//     Таких приборов должно быть, как минимум, два (например, настольная лампа и компьютер). Выбрав прибор, подумайте, какими свойствами он обладает.
//
// План:
//
// Определить родительскую функцию с методами, которые включают/выключают прибор из розетки.
//     Создать делегирующую связь [[Prototype]] для двух конкретных приборов.
//     У каждого из приборов должны быть собственные свойства и, желательно, методы, отличные от родительских методов.
//     Создать экземпляры каждого прибора.
//     Вывести в консоль и посмотреть результаты работы, гордиться собой. :)

class ElectricalAppliance {
    constructor(powerConsumption) {
        this.powerConsumption = powerConsumption
        this.isSwitchedOn = false
    }

    turnOn() {
        this.isSwitchedOn = true
    }

    turnOff() {
        this.isSwitchedOn = false
    }
}

class PC extends ElectricalAppliance {
    constructor(CPU, videocard, RAM, powerConsumption) {
        super(powerConsumption);
        this.CPU = CPU;
        this.videocard = videocard;
        this.RAM = RAM
        this.nowPlaying = 'Нет запущенных игр'
    }
    turnOn() {
        super.turnOn();
        console.log('Компьютер тихонько гудит')
    }
    turnOff() {
        super.turnOff();
        console.log('Выключаем компьютер')
    }

    startGame() {
        if (this.isSwitchedOn === true) {
            this.powerConsumption += 600
            let gamesList = ['Assassins Creed: Valhalla', 'World of Tanks', 'World of Warcraft', 'Horizon: Zero Dawn', 'Marvel\'s Guardians of the Galaxy'];
            let randomChoice = Math.floor(Math.random() * gamesList.length);
            let choosedGame = gamesList[randomChoice];
            this.nowPlaying = choosedGame
            console.log(`Запускаем ${choosedGame}. Кулер шумит сильнее...`)
        }
    }

    endGame() {
        this.powerConsumption -= 600
        console.log(`Выключаем ${this.nowPlaying}. Компьютер почти не шумит.`)
        this.nowPlaying = 'Нет запущенных игр'
    }

    getInfo() {
        console.log(`Статус: ${this.isSwitchedOn ? 'Включен' : 'Выключен'}
Потребляемая мощность: ${this.isSwitchedOn ? this.powerConsumption : 0} Вт
Процессор: ${this.CPU}
Видеокарта: ${this.videocard}
Оперативная память: ${this.RAM}
Запущена игра: ${this.nowPlaying}`)
    }
}

class Microwave extends ElectricalAppliance {
    constructor(brand, powerConsumption) {
        super(powerConsumption);
        this.brand = brand
        this.timer = 0
        this.isWorking = false
    }

    start() {
        if (this.isSwitchedOn === true) {

            this.timer = prompt('Выберите время подогрева от 1 до 300');
            if (this.timer <= 300 & this.timer >= 1) {
                this.isWorking = true
                console.log('Микроволновка гудит...')
                const microwaveWorking = setInterval(() => {
                    console.log(`${this.timer === 0 ? 'Дзынь!' : `До окончания: ${this.timer} сек`}`);
                    this.timer -= 1;
                    if (this.timer === -1) {
                        this.isWorking = false
                        clearInterval(microwaveWorking);
                    }
                }, 1000);
            } else {
                console.log('Выбрано некорректное время')
            }

        } else {
            console.log('Сначала подключите к сети!')
        }
    }

    stop() {
        this.timer = 0
        console.log(`Выключаем микроволновку ${this.brand} вручную`)
    }

    turnOn() {
        super.turnOn();
        console.log(`Подключаем микроволновку ${this.brand} к сети`)
    }

    turnOff() {
        super.turnOff();
        console.log(`Отключаем микроволновку ${this.brand} от сети`)
    }
    getInfo() {
        console.log(`Статус: 
${this.isSwitchedOn ? 'Подключена к сети' : 'Не подключена к сети'}
${this.isWorking ? `Запущена, времени до окончания работы: ${this.timer}` : 'Не запущена'}
${this.isWorking ? `Потребляемая мощность: ${this.powerConsumption} Вт` : 'Потребляемая мощность: 0 Вт'}`)
    }
}


const myPC = new PC('Intel(R) Core(TM) i5-10400', 'RTX 3080', '16GB', 200)
myPC.getInfo()
myPC.turnOn()
myPC.getInfo()
myPC.startGame()
myPC.getInfo()
myPC.endGame()
myPC.getInfo()
myPC.turnOff()
myPC.getInfo()

const myMicrowave = new Microwave('Scarlett', 1000)
myMicrowave.turnOn()
myMicrowave.start()
