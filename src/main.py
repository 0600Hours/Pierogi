import logging
from pathlib import Path
import yaml

DATA_PATH = Path(__file__).parent / 'data'
CONFIG_FILE = 'config.yaml'

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s | %(message)s',
)

with open((DATA_PATH / CONFIG_FILE).resolve()) as config_stream:
    config = yaml.safe_load(config_stream)

def run():
    logging.info(f'bot running under name {config["BOT_NAME"]}')