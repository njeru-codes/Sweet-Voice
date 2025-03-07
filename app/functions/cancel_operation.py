from telegram.ext import CallbackContext, ConversationHandler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup


async def cancel_operation(update: Update, context: CallbackContext):
    """Cancel the vFishing process."""
    keyboard = [
        [
            InlineKeyboardButton("Help", callback_data='help'),
            InlineKeyboardButton("Vfish", callback_data='vfish'),
        ]
    ]
    if update.message:
        await update.message.reply_text(
            'Vfish process canceled.'
            'Hello, welcome to Sweet Voice. \nThe best IVR red teaming tool. \n\nCredits: @njeru_mtwaiti',
            reply_markup=InlineKeyboardMarkup(keyboard)
            )
    elif update.callback_query:
        await update.callback_query.message.reply_text(
            'Vfish process canceled.'
            'Hello, welcome to Sweet Voice. \nThe best IVR red teaming tool. \n\nCredits: @njeru_mtwaiti',
            reply_markup=InlineKeyboardMarkup(keyboard))
        await update.callback_query.answer()

    return ConversationHandler.END

