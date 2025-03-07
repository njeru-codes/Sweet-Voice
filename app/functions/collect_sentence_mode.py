from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler

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
