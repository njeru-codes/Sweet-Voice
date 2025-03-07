from telegram import Update
from telegram.ext import CallbackContext
from functions.help_command import help_command
from functions.cancel_operation import cancel_operation
from functions.vfish import vfish

async def button(update: Update, context: CallbackContext):
    """Handle inline button clicks."""
    query = update.callback_query
    await query.answer()

    if query.data == 'help':
        await help_command(update, context)
    elif query.data == 'vfish':
        return await vfish(update, context)  # Calls vfish() properly
    elif query.data == 'cancel':
        return await cancel_operation(query, context)  # Calls cancel_operation() properly
