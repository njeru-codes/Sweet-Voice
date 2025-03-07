import sys
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, MessageHandler, filters,
    CallbackContext, CallbackQueryHandler, ConversationHandler
)
import os
from dotenv import load_dotenv
from functions.cancel_operation import cancel_operation
from functions.help_command import help_command
from functions.start import start
from functions.vfish import vfish
from functions.collect_victim_number import collect_victim_number
from functions.collect_victim_name import collect_victim_name
from functions.collect_service_name import collect_service_name
from functions.collect_voice_gender import collect_voice_gender
from functions.collect_sentence_mode import collect_sentence_mode
from functions.button_handler import button


load_dotenv()

TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
VICTIM_NUMBER, VICTIM_NAME, SERVICE_NAME, VOICE_GENDER, SENTENCE_MODE = range(5)


def main():
    try:
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

    except KeyboardInterrupt:
        print('Closing bot...')
        application.stop()
        sys.exit(0)
        
    except Exception as e:
        print("An error occurred:", e)
        sys.exit(1)
    finally:
        application.stop()
        sys.exit(0)
        print('Bot stopped')


if __name__ == "__main__":
    main()