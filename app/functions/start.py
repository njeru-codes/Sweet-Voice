from telegram.ext import CallbackContext, ConversationHandler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

async def start(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("Help", callback_data='help'),
            InlineKeyboardButton("Vfish", callback_data='vfish'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Hello, welcome to Sweet Voice. \nThe best IVR red teaming tool. \n\nCredits:  @njeru_mtwaiti",
        reply_markup=reply_markup
    )
