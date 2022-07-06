# command handlers for group commands

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, filters


async def handle_addquote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='quote added'
    )

handler_addquote = CommandHandler(
    'addquote',
    handle_addquote,
    filters.ChatType.GROUPS)
