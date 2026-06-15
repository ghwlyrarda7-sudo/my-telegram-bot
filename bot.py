import telebot
import os

API_TOKEN = os.environ.get('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

# قائمة الجولات
game_history = []

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! أرسل لي نتيجة الجولة (مثلاً: 1.50) لأحسب لك نسبة الاحتمالية.")

@bot.message_handler(func=lambda message: True)
def calculate_probability(message):
    try:
        val = float(message.text)
        game_history.append(val)
        if len(game_history) > 20: # نحتفظ بآخر 20 جولة فقط للتحليل الدقيق
            game_history.pop(0)
            
        # حساب نسبة الجولات التي فوق 2.0x
        high_rounds = [r for r in game_history if r >= 2.0]
        percentage = (len(high_rounds) / len(game_history)) * 100
        
        response = f"✅ تم تسجيل: {val}x\n"
        response += f"📊 إحصائية آخر {len(game_history)} جولات:\n"
        response += f"📈 نسبة صعود اللعبة فوق 2.0x هي: {percentage:.1f}%\n"
        
        if percentage > 50:
            response += "🔥 الحالة: اللعبة في وضع صعود قوي!"
        else:
            response += "🧊 الحالة: اللعبة في وضع حذر (انخفاض)."
            
        bot.reply_to(message, response)
    except:
        bot.reply_to(message, "أرسل رقماً صحيحاً فقط (مثلاً: 2.15)")

bot.infinity_polling()
