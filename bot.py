import os
import telebot

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

# Удаляем вебхук, чтобы polling заработал
bot.remove_webhook()

PRICE_PER_STAR = 280

# далее твой код бота... # 1 звезда = 280 сум

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
    bot.reply_to(message, f"{price:,} сум".replace(",", " "))

print("Бот запущен и работает 24/7...")
bot.infinity_polling()
