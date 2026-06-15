here@bot.message_handler(commands=['status'])
def send_status(message):
    if not history:
        bot.reply_to(message, "⚠️ لا توجد بيانات كافية. أرسل نتائج الجولات أولاً.")
        return
    
    avg = sum(history) / len(history)
    risk_level = "عالي جداً" if avg < 1.5 else "متوسط" if avg < 2.5 else "منخفض (آمن)"
    
    response = f"""
📊 **تحليل السيرفر الشخصي:**
📈 **عدد الجولات المسجلة:** {len(history)}
💰 **متوسط الانهيار:** {round(avg, 2)}x
🛡️ **حالة السوق:** {risk_level}
➖➖➖➖➖➖➖➖
نصيحة: إذا كانت الحالة "عالي جداً"، لا تدخل!
"""
    bot.reply_to(message, response)
