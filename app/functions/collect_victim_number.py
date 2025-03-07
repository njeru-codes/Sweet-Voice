from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

async def collect_victim_number(update: Update, context: CallbackContext):
    """Collect the victim's phone number and ask for the name."""
    keyboard = [
        [
            InlineKeyboardButton("cancel", callback_data='cancel'),
        ]
    ]
    context.user_data["victim_number"] = update.message.text
    await update.message.reply_text(
        "Enter The Victim Name:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
    return 1  # Return the next state (VICTIM_NAME)
