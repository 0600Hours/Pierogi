from src.handlers import all_handlers
import logging
from pathlib import Path
from telegram import Update
from telegram.ext import ApplicationBuilder
import yaml

DATA_PATH = Path(__file__).parent / 'data'
CONFIG_FILE = 'config.yaml'

# logging setup
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s | %(message)s',
)

# load config
with open((DATA_PATH / CONFIG_FILE).resolve()) as config_stream:
    config = yaml.safe_load(config_stream)

def run():
    application = ApplicationBuilder().token(config["BOT_TOKEN"]).build()

    application.add_handlers(all_handlers)
    application.run_polling()

    logging.info(f'bot running under name {config["BOT_NAME"]}')