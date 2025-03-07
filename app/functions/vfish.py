from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from functions.cancel_operation import cancel_operation

async def vfish(update: Update, context: CallbackContext):
    """Start the vFishing process and ask for victim number."""
    keyboard = [
        [
            InlineKeyboardButton("cancel", callback_data='cancel'),
        ]
    ]
    
    if update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.message.reply_text(
            "Enter The Victim Number:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    else:
        await update.message.reply_text(
            "Enter The Victim Number:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    return 0  # Return the first state (VICTIM_NUMBER)
