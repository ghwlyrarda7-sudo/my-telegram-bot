import telebot
import os

# ضع التوكن الخاص بك هنا بدلاً من 'YOUR_TOKEN_HERE'
# أو استخدم المتغير الذي أضفته في Railway
TOKEN = os.environ.get('API_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! البوت يعمل الآن بنجاح.")

print("البوت يعمل...")
bot.infinity_polling()
