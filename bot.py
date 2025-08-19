
import random
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# 🚨 ВАЖНО: Замени API_TOKEN на настоящий твой токен!
API_TOKEN = 'vk1.a.dyG2ZP7nxJ7v74Ij_xjuwtJbeh5MvCQVX6XYoVOAuM5iTKjQeUSdKIO1t_0jCQSh9MJ3M6VFXXElhmto2FW2G4nblh14HSyD9QHESn9yrl9e1k5ui-PmE6yVSuKsQ_ohzvRRWmX_fqdzAV0Du_lY-mJNGQE8Om-rxgzYoGS81_ni4aO4WnGckblnNsrSM5_8g5tpRatSAdTokxqW9dwwXA'  # ← Поставь свой токен сюда!

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# 📜 Список предсказаний
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

# 📢 Реклама AdFox (исправленные URL без пробелов!)
ads = [
    "<iframe src='https://adfox.ru/758968/1041184/iframe' width='300' height='250' frameborder='0'></iframe>",
    "<iframe src='https://adfox.ru/758968/1041185/iframe' width='300' height='250' frameborder='0'></iframe>",
    "<iframe src='https://adfox.ru/758968/1041186/iframe' width='300' height='250' frameborder='0'></iframe>",
    "<iframe src='https://adfox.ru/758968/1041187/iframe' width='300' height='250' frameborder='0'></iframe>"
]

# 🎯 Команда /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    ad = random.choice(ads)
    await message.answer(f"🔮 Привет! Я — бот-гадалка.\n\n"
                         f"{ad}\n\n"
                         f"Напиши /predict — я скажу, что будет!")

# 🧙‍♂️ Команда /predict
@dp.message(Command("predict"))
async def predict(message: types.Message):
    phrase = random.choice(gadalka)
    ad = random.choice(ads)
    await message.answer(f"🔮 {phrase}\n\n"
                         f"{ad}")

# 📝 Обработка текста (реакция на слова)
@dp.message()
async def handle_message(message: types.Message):
    text = message.text.lower()
    if "гадалка" in text or "прогноз" in text:
        await message.answer("Просто напиши /predict — я расскажу, что будет!")
    elif "поддержать" in text or "заработать" in text:
        await message.answer("💡 Хочешь зарабатывать? Создай свой бот — это легко и бесплатно!\n"
                             "Приходи в наш канал: @manga_gadalka — там всё объясняю!")

# 🛠 Запуск бота через вебхук
if __name__ == "__main__":
    from aiogram.webhook import WebhookServer
    import asyncio

    # Получаем PORT из переменных окружения (обязательно для Render!)
    PORT = int(os.environ.get("PORT", 80))

    # Настройка сервера
    server = WebhookServer(host="0.0.0.0", port=PORT)

    # Функция для обработки входящих обновлений
    async def handle_update(request):
        update = types.Update(**request.json())
        await dp.process_update(update)

    # Запуск сервера
    asyncio.run(server.run(
        handle_update=handle_update,
        on_startup=lambda: print("✅ Бот запущен!"),
        on_shutdown=lambda: print("❌ Бот остановлен")
    ))


