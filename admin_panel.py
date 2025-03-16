from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def get_admin_keyboard():
    keyboard = [
        [InlineKeyboardButton("📊 عرض الإحصائيات", callback_data="sta>
        [InlineKeyboardButton("👥 إدارة المستخدمين", callback_data="m>
        [InlineKeyboardButton("💰 مراجعة المدفوعات", callback_data="p>
    ]
    return InlineKeyboardMarkup(keyboard)
