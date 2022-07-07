import handlers
import logging
import os
import traceback
import yaml
from telegram.ext import ApplicationBuilder, CallbackContext
from telegram.error import (ChatMigrated, NetworkError, TelegramError)
from typing import Optional

# logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


# constants
CONFIG_FILENAME = 'config.yaml'


# core bot class
class PierogiCore:
    def __init__(self, config, handlers):
        self.app = ApplicationBuilder().token(config['BOT_TOKEN']).build()
        self.app.add_handlers(handlers)
        self.app.add_error_handler(self.handle_error)

    def handle_error(update: Optional[object], context: CallbackContext):
        try:
            raise context.error
        except ChatMigrated:  # taken care of in group migration handler
            pass
        except NetworkError:  # it's fine don't worry about it :)
            pass
        except TelegramError:
            logging.error(traceback.format_exc())

    def run(self):
        self.app.run_polling()


if __name__ == '__main__':
    logging.info('began running')

    # get config
    with open(os.path.join('data', CONFIG_FILENAME), 'r') as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as e:
            logging.error(e)
            quit()

    pierogiCore = PierogiCore(config, handlers.handlers)
    pierogiCore.run()
