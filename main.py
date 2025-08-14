# main.py — Точка входа для Render (с app)

from aiogram import Dispatcher, Bot
from bot import dp, bot
import os
import asyncio
from uvicorn import run

# Создаём объект app (обязательно!)
app = None  # Инициализируем

# Запуск сервера
async def main():
    print("🚀 Бот запущен!")
    await dp.start_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 80)),
        webhook_url=f"https://telegram-bot-gadalka.onrender.com/webhook"
    )

# Это обязательная строка — без неё uvicorn не найдёт app
if __name__ == "__main__":
    app = main  # Привязываем app к функции main
    asyncio.run(main())
