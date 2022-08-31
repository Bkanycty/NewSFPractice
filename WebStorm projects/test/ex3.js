const tri = document.getElementById("tri");
const tri_ctx = tri.getContext("2d");

tri_ctx.beginPath(); // Создает новый контур
tri_ctx.moveTo(75,50); // Перемещает перо в точку с координатами x и y.
tri_ctx.lineTo(100,75); // Рисует линию с текущей позиции до позиции, определенной x и y.
tri_ctx.lineTo(100,25);
tri_ctx.fillStyle = "green"; // Заливаем выбранным цветом фигуру
tri_ctx.fill(); // Рисует фигуру с заливкой внутренней области.
