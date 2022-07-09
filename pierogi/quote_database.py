'''Define quote database object and functions for interacting with it'''

import os
from util.db_classes import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class QuoteDatabase:
    '''
    Quote database master class

    :attr str filename: database filename location
    :attr sessionmaker session_factory: SQLAlchemy object for initiating sessions
    '''

    def __init__(self, filename='quotes.db'):
        '''
        Quote database constructor

        :param str filename: file location of the quote database
        '''
        self.filename = filename

        engine = create_engine(f'sqlite:///{os.path.join("data", filename)}')
        Base.metadata.create_all(engine)

        self.session_factory = sessionmaker(engine)
