import logging
from telegram.ext import ApplicationBuilder
import yaml

# logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


# core bot class
class Pierogi:
    def __init__(self, config, handlers):
        self.app = ApplicationBuilder().token(config['BOT_TOKEN']).build()
        self.app.addHandlers(handlers)

    def run(self):
        self.app.run_polling()


if __name__ == '__main__':
    from pierogi.handlers import handlers

    logging.info('began running')

    # get config
    with open('config.yaml', 'r') as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as e:
            logging.error(e)
            quit()

    pierogi = Pierogi(config, handlers)
    pierogi.run()
