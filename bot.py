import os
from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

WEBAPP_URL = "https://web-production-b0fda.up.railway.app/webapp/index.html"  # URL твоего Web App

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Открыть мини-приложение", web_app=WebAppInfo(url=WEBAPP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Привет! Нажми кнопку ниже, чтобы открыть мини-приложение:", reply_markup=reply_markup)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен...")
    app.run_polling()
