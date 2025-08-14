import telebot

# ВАШ ТОКЕН
TOKEN = "8326581351:AAEj3wqCMQpQO2SLX_kX0XqLJnxG8p8ZFDI"
bot = telebot.TeleBot(TOKEN)

PRICE_PER_STAR = 280  # 1 звезда = 280 сум (так как 50 звезд = 14,000)

# Ответ на сообщение "1"
@bot.message_handler(func=lambda m: m.text and m.text.strip() == "1")
def reply_one(message):
    bot.reply_to(message, "https://t.me/mmpremiumm/9")

# Ответ на сообщение "2"
@bot.message_handler(func=lambda m: m.text and m.text.strip() == "2")
def reply_two(message):
    bot.reply_to(message, "https://t.me/mmpremiumm/10")

# Если ввели число больше 50 — считаем цену
@bot.message_handler(func=lambda m: m.text and m.text.strip().isdigit() and int(m.text.strip()) > 50)
def reply_price(message):
    stars = int(message.text.strip())
    price = stars * PRICE_PER_STAR
    bot.reply_to(message, f"{price:,} сум".replace(",", " "))  # форматируем с пробелами

print("Бот запущен и работает 24/7...")
bot.infinity_polling()  # работает без остановки
