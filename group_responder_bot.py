import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.environ["BOT_TOKEN"]
RESPONSE_TEXT = "Hello! I'm a bot responding to every message in this group."

async def respond(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(RESPONSE_TEXT)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.GROUPS, respond))

print("Bot is running...")
app.run_polling()
