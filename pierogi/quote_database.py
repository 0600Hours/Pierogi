'''Definte quote database object and functions for interacting with it'''


class QuoteDatabase:
    '''
    Quote Database constructor

    :param str filename: database filename
    '''
    def init(self, filename='quotes.db'):
        self.filename = filename
