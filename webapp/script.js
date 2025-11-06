const btn = document.getElementById("sendDataBtn");

btn.addEventListener("click", () => {
    if (window.Telegram.WebApp) {
        Telegram.WebApp.sendData("Привет, бот! Это данные из Web App.");
        alert("Данные отправлены боту!");
    } else {
        alert("Telegram Web App не доступен!");
    }
});
