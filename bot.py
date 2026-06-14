import telebot
import os

# Get the token from environment variables
API_TOKEN = os.environ.get('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

# Handle the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "البوت يعمل الآن بنجاح!")

print("Bot is running...")

# Keep the bot running
bot.infinity_polling()
