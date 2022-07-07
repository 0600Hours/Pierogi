# command handlers for group commands

import re
import itertools
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, filters

# emoji definitions
LOUDLY_CRYING_FACE = '\U0001F62D'
POUTING_FACE = '\U0001F621'
SMILING_FACE_WITH_SUNGLASSES = '\U0001F60E'
SMILING_FACE_WITH_OPEN_MOUTH = '\U0001F603'
FROWNING_FACE = '\U00002639'
FAMILY_MAN_GIRL_BOY = '\U0001F468\U0000200D\U0001F467\U0000200D\U0001F466'
FLEXED_BICEPS = '\U0001F4AA'
VAMPIRE = '\U0001F9DB'
GRADUATION_CAP = '\U0001F393'


# possible command prefixes and their emojis
COMMAND_PREFIXES = {
    'add': None,
    'mad': POUTING_FACE,
    'sad': LOUDLY_CRYING_FACE,
    'rad': SMILING_FACE_WITH_SUNGLASSES,
    'glad': SMILING_FACE_WITH_OPEN_MOUTH,
    'bad': FROWNING_FACE,
    'dad': FAMILY_MAN_GIRL_BOY,
    'chad': FLEXED_BICEPS,
    'vlad': VAMPIRE,
    'grad': GRADUATION_CAP,
}

# possible command suffixes
COMMAND_SUFFIXES = ['quote', 'qoute']


# properly formats a word with optional emojis
def format_response(s, emoji):
    if emoji is not None:
        return f' {emoji} '.join(s.split(' '))
    return s


def generate_commands():
    return list(map(''.join, list(itertools.product(COMMAND_PREFIXES.keys(), COMMAND_SUFFIXES))))


# add a quote to the db
async def handle_addquote(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE):
    # isolate command name
    message = update.message
    command_text = re.split('/|@| ', message.text, 2)[1]

    # find prefix
    for prefix in COMMAND_PREFIXES:
        if command_text.startswith(prefix):
            command_prefix = prefix
            break

    # determine noun, verb, and emoji for given command
    if command_prefix is not None:
        noun = command_text[len(command_prefix):]
        verb = f'{command_prefix}ded'.replace('ddd', 'dd')
        emoji = COMMAND_PREFIXES[command_prefix]
    else:
        noun = 'quote'
        verb = 'added'
        emoji = None

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=format_response(f'{noun} {verb}', emoji)
    )


# # addquote variants
# async def handle_addqoute(
#         update: Update,
#         context: ContextTypes.DEFAULT_TYPE):
#     await handle_addquote(update, context, noun='qoute')


# async def handle_madquote(
#         update: Update,
#         context: ContextTypes.DEFAULT_TYPE):
#     await handle_addquote(update, context, verb='madded', emoji=POUTING_FACE)


# async def handle_sadquote(
#         update: Update,
#         context: ContextTypes.DEFAULT_TYPE):
#     await handle_addquote(update, context, verb='sadded', emoji=LOUDLY_CRYING_FACE)


# async def handle_radquote(
#         update: Update,
#         context: ContextTypes.DEFAULT_TYPE):
#     await handle_addquote(update, context, verb='radded', emoji=SMILING_FACE_WITH_SUNGLASSES)


# async def handle_gladquote(
#         update: Update,
#         context: ContextTypes.DEFAULT_TYPE):
#     await handle_addquote(update, context, verb='gladded', emoji=SMILING_FACE_WITH_OPEN_MOUTH)


# async def handle_badquote(
#         update: Update,
#         context: ContextTypes.DEFAULT_TYPE):
#     await handle_addquote(update, context, verb='badded', emoji=FROWNING_FACE)


# async def handle_dadquote(
#         update: Update,
#         context: ContextTypes.DEFAULT_TYPE):
#     await handle_addquote(update, context, verb='dadded', emoji=FAMILY_MAN_GIRL_BOY)


# handler definitions
handler_addquote = CommandHandler(
    generate_commands(),
    handle_addquote,
    filters.ChatType.GROUPS)

# handler_addqoute = CommandHandler(
#     'addqoute',
#     handle_addqoute,
#     filters.ChatType.GROUPS)

# handler_madquote = CommandHandler(
#     'madquote',
#     handle_madquote,
#     filters.ChatType.GROUPS)

# handler_sadquote = CommandHandler(
#     'sadquote',
#     handle_sadquote,
#     filters.ChatType.GROUPS)

# handler_radquote = CommandHandler(
#     'radquote',
#     handle_radquote,
#     filters.ChatType.GROUPS)

# handler_gladquote = CommandHandler(
#     'gladquote',
#     handle_gladquote,
#     filters.ChatType.GROUPS)

# handler_badquote = CommandHandler(
#     'badquote',
#     handle_badquote,
#     filters.ChatType.GROUPS)

# handler_dadquote = CommandHandler(
#     'dadquote',
#     handle_dadquote,
#     filters.ChatType.GROUPS)
