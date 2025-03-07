from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

async def collect_service_name(update: Update, context: CallbackContext):
    """Collect the service name and ask for voice gender."""
    keyboard = [
        [
            InlineKeyboardButton("cancel", callback_data='cancel'),
        ]
    ]
    context.user_data["service_name"] = update.message.text
    await update.message.reply_text(
        "Choose Voice Gender: Woman / Man (W/M)",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
    return 3  # Return the next state (VOICE_GENDER)
