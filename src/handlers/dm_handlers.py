from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Start message recieved, still setting this up.")    

handler_start = CommandHandler('start', start, filters.ChatType.PRIVATE)

handlers = [handler_start]