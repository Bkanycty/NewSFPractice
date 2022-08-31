const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

ctx.fillStyle = "gray";
ctx.fillRect(0, 0, 300, 300);

// Полый прямоугольник
ctx.strokeStyle = "yellow"; // Цвет границ прямоугольника
ctx.strokeRect(10, 20, 30, 40); // Метод отрисовки полого прямоугольника

// Залитый прямоугольник
ctx.fillStyle = "green"; // Цвет залитого прямоугольника
ctx.fillRect(70, 10, 50, 50); // Метод отрисовки залитого прямоугольника