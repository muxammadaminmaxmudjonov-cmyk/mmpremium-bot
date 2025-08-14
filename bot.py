import os
import telebot

# Получаем токен из переменных окружения Render
TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# Функция пересчёта звёзд в сумму
def stars_to_money(stars: int) -> int:
    # 50 звёзд = 14 000 сум
    # Считаем пропорционально
    money = (stars * 14000) // 50
    return money

# Обработчик сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.strip()
    if text.isdigit():  # Если пользователь пишет только цифры
        stars = int(text)
        money = stars_to_money(stars)
        bot.send_message(message.chat.id, f"{stars} звёзд → {money} сум")
    else:
        bot.send_message(message.chat.id, "Пиши только число звёзд.")

# Запуск бота 24/7
if __name__ == "__main__":
    print("Бот запущен и работает 24/7 на Render!")
    bot.infinity_polling()
