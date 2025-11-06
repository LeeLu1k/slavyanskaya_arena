const btn = document.getElementById("sendDataBtn");

btn.addEventListener("click", () => {
    // Отправляем данные боту
    if (window.Telegram.WebApp) {
        Telegram.WebApp.sendData("Привет, бот! Это данные из Web App.");
        alert("Данные отправлены боту!");
    }
});
