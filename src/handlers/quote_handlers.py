from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

# add quote
async def add_quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Add quote")

handler_add_quote = CommandHandler('addquote', add_quote)

# find random quote
async def random_quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Random quote")

handler_random_quote = CommandHandler('random', random_quote)

handlers = [handler_add_quote, handler_random_quote]