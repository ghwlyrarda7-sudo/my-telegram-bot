import telebot
import os

# جلب التوكن من المتغيرات في Railway
API_TOKEN = os.environ.get('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

# معالج الأمر /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "البوت يعمل الآن بنجاح.")

print("البوت يعمل الآن وينتظر الرسائل...")

# تشغيل البوت بشكل مستمر
bot.infinity_polling()
