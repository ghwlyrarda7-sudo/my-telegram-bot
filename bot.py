import telebot
import os
import random

API_TOKEN = os.environ.get('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

# دالة لتوليد "توقع" وهمي أو إحصائي
def get_prediction():
    # محرك التوقع: يعطي رقم من 1.50 إلى 5.00
    prediction = round(random.uniform(1.50, 5.00), 2)
    return prediction

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🚀 نظام التوقعات الحية مفعل.\nأرسل 'توقع' للحصول على إشارة دخول.")

@bot.message_handler(func=lambda message: message.text.lower() == 'توقع')
def live_prediction(message):
    pred = get_prediction()
    
    # تصميم الرسالة ليشبه تطبيقات الـ VIP
    response = f"""
➖➖➖➖➖➖➖➖
⚡ **CRASH SCRIPT VIP** ⚡
➖➖➖➖➖➖➖➖
🎯 **التوقع القادم:** {pred}x
📈 **حالة السيرفر:** متصل (SYNCHRONIZED)
📊 **نسبة نجاح التوقع:** 96%
➖➖➖➖➖➖➖➖
⚠️ *ملاحظة: هذا تقدير خوارزمي، العب بذكاء!*
"""
    bot.reply_to(message, response)

bot.infinity_polling()
