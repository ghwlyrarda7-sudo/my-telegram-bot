here# هذا الكود هو المسؤول عن استقبال الأرقام منك
@bot.message_handler(func=lambda message: message.text.replace('.', '', 1).isdigit())
def handle_numbers(message):
    val = float(message.text)
    history.append(val)
    if len(history) > 20: history.pop(0) # الاحتفاظ بآخر 20 جولة فقط
    
    # حساب نسبة النجاح (مثال: كم مرة كان الرقم فوق 2.0)
    above_2 = len([x for x in history if x >= 2.0])
    percent = (above_2 / len(history)) * 100
    
    response = f"✅ تم تسجيل {val}x.\n📊 إحصائية آخر {len(history)} جولات:\n📈 نسبة صعود اللعبة فوق 2.0 هي: {percent}%\n🔥 الحالة: {'وضع صعود قوي' if percent > 50 else 'حالة غير مستقرة'}"
    bot.reply_to(message, response)
