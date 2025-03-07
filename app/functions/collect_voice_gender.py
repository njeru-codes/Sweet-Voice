from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

async def collect_voice_gender(update: Update, context: CallbackContext):
    """Collect the preferred voice gender and ask for sentence mode."""
    keyboard = [
        [
            InlineKeyboardButton("cancel", callback_data='cancel'),
        ]
    ]
    context.user_data["voice_gender"] = update.message.text.upper()
    await update.message.reply_text(
        "If you want to use your sentences, write 'manual - your sentences' or write 'auto'.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
    return 4  # Return the next state (SENTENCE_MODE)
