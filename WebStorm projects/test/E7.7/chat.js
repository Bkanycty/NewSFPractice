const wsUrl = "wss://echo.websocket.org/";
let websocket = new WebSocket(wsUrl);


const btnSend = document.getElementById("send-button");


function writeToScreen(message) {
    let chatBox = document.getElementById("chat-box");
    chatBox.insertAdjacentHTML('beforeend', `<p> ${message}</p>`);
    websocket.send(message)
}


btnSend.addEventListener('click', () => {
    const message = 'Test message';
    writeToScreen(message);
    websocket.send(message);
});

websocket.onopen = function(e) {
    let status = document.getElementById("input-form")
    status.insertAdjacentHTML("beforebegin", "<p>Connected</p>")
}

websocket.onmessage = function(evt) {
    writeToScreen(
        '<p>RESPONSE: ' + evt.data+'</p>'
    );
};
websocket.onerror = function(evt) {
    writeToScreen(
        '<span style="color: red;">ERROR:</span> ' + evt.data
    );
};
console.log(websocket)