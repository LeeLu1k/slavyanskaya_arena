from flask import Flask
import threading
import telebot
import os

app = Flask(__name__)

# --- Flask сервер ---
@app.route("/")
def index():
    return "Славянская арена Web App работает!"

# --- Telegram бот ---
TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Бот работает!")

def run_bot():
    bot.polling()

# --- Запуск ---
if __name__ == "__main__":
    # запускаем бот в отдельном потоке
    threading.Thread(target=run_bot).start()

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
