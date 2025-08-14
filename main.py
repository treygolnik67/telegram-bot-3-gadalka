# main.py — Точка входа для Render

from aiogram import Dispatcher, Bot
from bot import dp, bot
import os
import asyncio
from uvicorn import run

# Запуск сервера
async def main():
    print("🚀 Бот запущен!")
    await dp.start_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 80)),
        webhook_url=f"https://telegram-bot-gadalka.onrender.com/webhook"
    )

if __name__ == "__main__":
    asyncio.run(main())