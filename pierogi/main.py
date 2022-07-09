import handlers
import logging
import os
import sys
import traceback
import yaml
from quote_database import QuoteDatabase
from telegram.ext import ApplicationBuilder, CallbackContext
from telegram.error import (ChatMigrated, NetworkError, TelegramError)
from typing import Optional

# check for debug mode
DEBUG = any(arg in sys.argv[1:] for arg in ['-d', '--debug'])

# logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


# constants
CONFIG_FILENAME = 'config.yaml'
DATABASE_FILENAME = 'quotes.db' if not DEBUG else 'quotes_test.db'

# init database
quote_database = QuoteDatabase(DATABASE_FILENAME)


class PierogiCore:
    '''
    Core bot class, through which everything else runs

    :attr Application app: telegram library application object
    '''

    def __init__(self, config, handlers):
        '''
        PierogiCore constructor

        :param dict config: contents of the config file
        :param List[BaseHandler] handlers: all handlers needed to process updates
        '''
        self.app = ApplicationBuilder().token(config['BOT_TOKEN']).build()
        self.app.add_handlers(handlers)
        self.app.add_error_handler(self.handle_error)

    def handle_error(update: Optional[object], context: CallbackContext):
        '''
        General error handler for all updates
        '''
        try:
            raise context.error
        except ChatMigrated:  # taken care of in group migration handler
            pass
        except NetworkError:  # it's fine don't worry about it :)
            pass
        except TelegramError:
            logging.error(traceback.format_exc())

    def run(self):
        '''
        Begin running the bot and waiting for updates from telegram
        '''
        self.app.run_polling()


if __name__ == '__main__':
    logging.info(f'began running. debug mode: {DEBUG}')

    # get config
    with open(os.path.join('data', CONFIG_FILENAME), 'r') as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as e:
            logging.error(e)
            quit()

    pierogiCore = PierogiCore(config, handlers.handlers)
    pierogiCore.run()
