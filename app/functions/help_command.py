from telegram.ext import CallbackContext, ConversationHandler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

async def help_command(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("Help", callback_data='help'),
            InlineKeyboardButton("vfish", callback_data='vfish'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        await update.message.reply_text(
            'Hello, welcome to Sweet Voice\n\n'
            'Commands:\n'
            '/start - Welcome message and commands.\n'
            '/help - Get information on how to use the bot.\n'
            '/vfish - Start a Voice Phishing simulation.',
            reply_markup=reply_markup
        )
    elif update.callback_query:
        await update.callback_query.message.reply_text(
            'Hello, welcome to Sweet Voice\n\n'
            'Commands:\n'
            '/start - Welcome message and commands.\n'
            '/help - Get information on how to use the bot.\n'
            '/vfish - Start a Voice Phishing simulation.',
            reply_markup=reply_markup
        )
        await update.callback_query.answer()