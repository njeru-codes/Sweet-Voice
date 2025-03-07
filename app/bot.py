import sys
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram.ext import CallbackContext, CallbackQueryHandler, ConversationHandler

import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')

def main():
    application = Application.builder().token(TELEGRAM_API_TOKEN).build()

    application.run_polling()


async def help_command(update: Update, context: CallbackContext):
    pass

async def start(update: Update, context: CallbackContext):
    pass

async def vfish(update: Update, context: CallbackContext):
    pass

async def collect_victim_number(update: Update, context: CallbackContext):
    pass

async def collect_victim_name(update: Update, context: CallbackContext):
    pass

async def collect_service_name(update: Update, context: CallbackContext):
    pass

async def collect_voice_gender(update: Update, context: CallbackContext):
    pass

async def collect_sentence_mode(update: Update, context: CallbackContext):
    pass

async def cancel_operation(update: Update, context: CallbackContext):
    pass

async def button(update: Update, context: CallbackContext):
    pass


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('closing boat')
        sys.exit(0)
    except Exception as e:
        print("An error occurred")
        print(e)
        sys.exit(1)
    
