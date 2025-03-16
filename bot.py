from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
from database import init_db, add_user, log_payment
from image_processor import enhance_image
import config

def start(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    add_user(user_id)
    update.message.reply_text("👋 مرحبًا بك! أرسل صورة لتحسين دقتها.")

def process_image(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    photo = update.message.photo[-1].get_file()
    file_path = f"photo_{user_id}.jpg"
    photo.download(file_path)

    keyboard = [[InlineKeyboardButton("🔹 2X", callback_data=f"enhance_2_{file_path}"),
                 InlineKeyboardButton("🔹 4X", callback_data=f"enhance_4_{file_path}"),
                 InlineKeyboardButton("🔹 8X", callback_data=f"enhance_8_{file_path}")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text("📈 اختر مستوى الدقة:", reply_markup=reply_markup)

def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    data = query.data.split("_")
    scale = int(data[1])
    image_path = data[2]

    enhanced_path = enhance_image(image_path, scale)
    query.message.reply_photo(photo=open(enhanced_path, "rb"), caption=f"✅ تم تحسين الصورة بدقة {scale}X!")

def main():
    init_db()
    updater = Updater(config.TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.photo, process_image))
    dp.add_handler(CallbackQueryHandler(button_handler))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
