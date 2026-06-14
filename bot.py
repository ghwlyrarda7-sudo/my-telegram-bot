import os
import telebot

TOKEN = os.environ.get('API_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "تم التشغيل بنجاح! البوت يعمل الآن.")

bot.polling()
