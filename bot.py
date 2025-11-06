import telebot
import os

TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)

WEB_APP_URL = os.getenv('WEB_APP_URL')  # URL вашего Web App, например Railway

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    web_app_button = telebot.types.KeyboardButton(
        text="Открыть арену",
        web_app=telebot.types.WebAppInfo(url=WEB_APP_URL)
    )
    markup.add(web_app_button)
    bot.send_message(message.chat.id, "Добро пожаловать в Славянскую арену! Откройте веб-приложение ниже:", reply_markup=markup)

bot.polling()
