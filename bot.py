# كود لربط البوت بالسجل الشخصي للمستخدم
user_history = {} # قاموس لتخزين نتائج كل مستخدم على حدة

@bot.message_handler(func=lambda message: message.text.replace('.', '', 1).isdigit())
def register_user_result(message):
    user_id = message.from_user.id
    val = float(message.text)
    
    # حفظ نتائج كل مستخدم في قائمة خاصة به فقط
    if user_id not in user_history:
        user_history[user_id] = []
    
    user_history[user_id].append(val)
    if len(user_history[user_id]) > 10: user_history[user_id].pop(0) # الاحتفاظ بآخر 10 نتائج فقط
    
    bot.reply_to(message, "✅ تم تسجيل النتيجة في سجل حسابك الخاص.")

@bot.message_handler(func=lambda message: message.text.lower() == 'توقع')
def personal_predict(message):
    user_id = message.from_user.id
    if user_id not in user_history or len(user_history[user_id]) < 3:
        bot.reply_to(message, "⚠️ يرجى تزويدي بـ 3 نتائج ظهرت في حسابك أولاً.")
        return

    # تحليل "سلوك" حسابك الخاص
    personal_data = user_history[user_id]
    prediction = (sum(personal_data) / len(personal_data)) * 1.15
    
    bot.reply_to(message, f"🎯 **توقع خاص بحسابك (ID: {user_id}):** {round(prediction, 2)}x")
