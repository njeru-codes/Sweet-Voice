import sys
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, MessageHandler, filters,
    CallbackContext, CallbackQueryHandler, ConversationHandler
)
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
VICTIM_NUMBER, VICTIM_NAME, SERVICE_NAME, VOICE_GENDER, SENTENCE_MODE = range(5)


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


async def start(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("Help", callback_data='help'),
            InlineKeyboardButton("Vfish", callback_data='vfish'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Hello, welcome to Sweet Voice. \nThe best IVR red teaming tool. \nCredits: @github @njeru-codes",
        reply_markup=reply_markup
    )


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
            reply_markup = InlineKeyboardMarkup(keyboard)
            )
    else:
        await update.message.reply_text(
            "Enter The Victim Number:",
            reply_markup = InlineKeyboardMarkup(keyboard)
            )

    return VICTIM_NUMBER


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
        reply_markup = InlineKeyboardMarkup(keyboard)
        )
    return VICTIM_NAME


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
        reply_markup = InlineKeyboardMarkup(keyboard)
        )
    return SERVICE_NAME


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
        reply_markup = InlineKeyboardMarkup(keyboard)
        )
    return VOICE_GENDER


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
        reply_markup = InlineKeyboardMarkup(keyboard)
    )
    return SENTENCE_MODE


async def collect_sentence_mode(update: Update, context: CallbackContext):
    """Collect sentence mode and display summary."""
    context.user_data["sentence_mode"] = update.message.text.lower()

    summary = (
        f"✅ Voice Phishing Simulation Started!\n\n"
        f"📞 Victim Number: {context.user_data['victim_number']}\n"
        f"👤 Victim Name: {context.user_data['victim_name']}\n"
        f"🏢 Service Name: {context.user_data['service_name']}\n"
        f"🎙 Voice Type: {context.user_data['voice_gender']}\n"
        f"📝 Sentence Mode: {context.user_data['sentence_mode']}\n\n"
        f"⚠️ Please wait while we simulate the attack..."
    )

    await update.message.reply_text(summary)
    return ConversationHandler.END


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
            'Hello, welcome to Sweet Voice. \nThe best IVR red teaming tool. \nCredits: @njeru-codes',
            reply_markup=InlineKeyboardMarkup(keyboard)
            )
    elif update.callback_query:
        await update.callback_query.message.reply_text(
            'Vfish process canceled.'
            'Hello, welcome to Sweet Voice. \nThe best IVR red teaming tool. \nCredits: @njeru-codes',
            reply_markup=InlineKeyboardMarkup(keyboard))
        await update.callback_query.answer()

    return ConversationHandler.END



async def button(update: Update, context: CallbackContext):
    """Handle inline button clicks."""
    query = update.callback_query
    await query.answer()

    if query.data == 'help':
        await help_command(update, context)
    elif query.data == 'vfish':
        return await vfish(update, context)  # **Fixed: Calls vfish() properly**
    elif query.data == 'cancel':
        return await cancel_operation(query, context)  # Pass query directly



def main():
    application = Application.builder().token(TELEGRAM_API_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('vfish', vfish), CallbackQueryHandler(button, pattern='^vfish$')],
        states={
            VICTIM_NUMBER: [MessageHandler(filters.TEXT & ~filters.COMMAND, collect_victim_number)],
            VICTIM_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, collect_victim_name)],
            SERVICE_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, collect_service_name)],
            VOICE_GENDER: [MessageHandler(filters.TEXT & ~filters.COMMAND, collect_voice_gender)],
            SENTENCE_MODE: [MessageHandler(filters.TEXT & ~filters.COMMAND, collect_sentence_mode)],
        },
        fallbacks=[CommandHandler("cancel", cancel_operation)],
    )

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(conv_handler)
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Closing bot...')
        sys.exit(0)
    except Exception as e:
        print("An error occurred:", e)
        sys.exit(1)
