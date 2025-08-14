import os
import telebot
import time

# Получаем токен из переменной окружения
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

# Удаляем старый вебхук и старые polling сессии
bot.remove_webhook()
time.sleep(1)  # ждём, чтобы Telegram успел обработать
bot.stop_polling()

PRICE_PER_STAR = 280  # 1 звезда = 280 сум

# Обработчик для сообщения "1"
@bot.message_handler(func=lambda m: m.text and m.text.strip() == "1")
def reply_one(message):
    bot.reply_to(message, "https://t.me/mmpremiumm/9")

# Обработчик для сообщения "2"
@bot.message_handler(func=lambda m: m.text and m.text.strip() == "2")
def reply_two(message):
    bot.reply_to(message, "https://t.me/mmpremiumm/10")

# Обработчик для чисел >50
@bot.message_handler(func=lambda m: m.text and m.text.strip().isdigit() and int(m.text.strip()) > 50)
def reply_price(message):
    stars = int(message.text.strip())
    price = stars * PRICE_PER_STAR
    bot.reply_to(message, f"{price:,} сум".replace(",", " "))

print("Бот запущен и работает 24/7...")

# Infinity polling с автоматическим перезапуском при ошибках
while True:
    try:
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    except Exception as e:
        print(f"Ошибка: {e}, перезапуск через 5 секунд")
        time.sleep(5)
