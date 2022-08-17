/* Этап 1. Подготовка данных */

// Создание экземпляра класса DOMParser. Он позволит нам парсить XML
const parser = new DOMParser();
// console.log('parser', parser);

// XML, который мы будем парсить
const xmlString = `
  <list>
    <student>
        <name lang="en">
            <first>Ivan</first>
            <second>Ivanov</second>
        </name>
        <age>35</age>
        <prof>teacher</prof>
    </student>
    <student>
        <name lang="ru">
            <first>Петр</first>
            <second>Петров</second>
        </name>
        <age>58</age>
        <prof>driver</prof>
    </student>
  </list>
`;
// console.log('xmlString', xmlString);

/* Этап 2. Получение данных */

// Парсинг XML
const xmlDOM = parser.parseFromString(xmlString, "text/xml");

// Получение всех DOM-нод
const listNode = xmlDOM.querySelector("list");
// const titleNode = bookNode.querySelector("title");
// const authorNode = bookNode.querySelector("author");
// const yearNode = bookNode.querySelector("year");
// const priceNode = bookNode.querySelector("price");
console.log('listNode', listNode.childNodes);




// // Получение данных из атрибутов
// const categoryAttr = bookNode.getAttribute('category');
// const langAttr = titleNode.getAttribute('lang');
// // console.log('categoryAttr', categoryAttr);
// // console.log('langAttr', langAttr);
//
// /* Этап 3. Запись данных в результирующий объект */
// const result = {
//     category: categoryAttr,
//     lang: langAttr,
//     title: titleNode.textContent,
//     author: authorNode.textContent,
//     year: Number(yearNode.textContent),
//     price: Number(priceNode.textContent),
// };
// console.log('result', result);
//
