from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

async def collect_victim_name(update: Update, context: CallbackContext):
    """Collect the victim's name and ask for the service name."""
    keyboard = [
        [
            InlineKeyboardButton("cancel", callback_data='cancel'),
        ]
    ]
    context.user_data["victim_name"] = update.message.text
    await update.message.reply_text(
        "Enter the Service Name:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
    return 2  # Return the next state (SERVICE_NAME)
