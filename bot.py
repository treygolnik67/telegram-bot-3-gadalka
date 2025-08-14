# bot.py — Основной бот

import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

API_TOKEN = '8224578219:AAHxTrnO4nc28QXgmEsEAqniwYi5MeTwwos'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

gadalka = [
    "Тебе повезёт сегодня!",
    "Сегодня день удачи!",
    "Планируй встречу с коллегой.",
    "Запиши идею — она может стать великим проектом.",
    "Сегодня лучше не выходить на улицу.",
    "У тебя будет отличное настроение!",
    "Сегодня ты сделаешь важный шаг вперёд.",
    "Будь готов к неожиданному подарку.",
    "Твой день будет полон позитива!",
    "Сегодня удача улыбнётся тебе.",
    "Все начинания пройдут успешно.",
    "Ты найдёшь решение сложной задачи.",
    "Твои мечты скоро сбудутся.",
    "Сегодня ты сделаешь что-то значимое.",
    "У тебя всё получится — верь в себя!"
]

# 📢 Реальная реклама (AdFox)
ads = [
    "<iframe src='https://adfox.ru/758968/1041184/iframe' width='300' height='250' frameborder='0'></iframe>",
    "<iframe src='https://adfox.ru/758968/1041185/iframe' width='300' height='250' frameborder='0'></iframe>",
    "<iframe src='https://adfox.ru/758968/1041186/iframe' width='300' height='250' frameborder='0'></iframe>",
    "<iframe src='https://adfox.ru/758968/1041187/iframe' width='300' height='250' frameborder='0'></iframe>"
]

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    ad = random.choice(ads)
    await message.answer(f"🔮 Привет! Я — бот-гадалка.\n\n"
                         f"{ad}\n\n"
                         f"Напиши /predict — я скажу, что будет!")

@dp.message(Command("predict"))
async def predict(message: types.Message):
    phrase = random.choice(gadalka)
    ad = random.choice(ads)
    await message.answer(f"🔮 {phrase}\n\n"
                         f"{ad}")

@dp.message()
async def handle_message(message: types.Message):
    text = message.text.lower()
    if "гадалка" in text or "прогноз" in text:
        await message.answer("Просто напиши /predict — я расскажу, что будет!")
    elif "поддержать" in text or "заработать" in text:
        await message.answer("💡 Хочешь зарабатывать? Создай свой бот — это легко и бесплатно!\n"
                             "Приходи в наш канал: @manga_gadalka — там всё объясняю!")

# --- Запуск ---
if __name__ == "__main__":
    from aiogram.webhook import WebhookServer
    import asyncio
    server = WebhookServer(host="0.0.0.0", port=int(os.environ.get("PORT", 80)))
    asyncio.run(server.run(
        handle_update=lambda request: dp.process_update(types.Update(**request.json())),
        on_startup=lambda: print("Бот запущен"),
        on_shutdown=lambda: print("Бот остановлен")
    ))

