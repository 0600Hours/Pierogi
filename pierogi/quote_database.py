'''Define quote database object and functions for interacting with it'''

import os
from util.db_classes import Base, Chat, Quote, User
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.sql import exists


class QuoteDatabase:
    '''
    Quote database master class

    :attr str filename: database filename location
    :attr sessionmaker session_factory: SQLAlchemy object for initiating sessions
    '''
    # Status codes for adding quotes
    QUOTE_SUCCESSFULLY_ADDED = 1
    QUOTE_ALREADY_EXISTS = 2
    QUOTE_PREVIOUSLY_DELETED = 3

    def __init__(self, filename='quotes.db'):
        '''
        Quote database constructor

        :param str filename: file location of the quote database
        '''
        self.filename = filename

        engine = create_engine(f'sqlite:///{os.path.join("data", filename)}')
        Base.metadata.create_all(engine)

        self.session_factory = sessionmaker(engine)

    def create_session(self, **kwargs):
        '''Create a session for interacting with the database'''
        return self.session_factory(**kwargs)

    # user methods
    def user_exists(self, session: Session, user_id):
        '''Test whether or not a user exists in the database'''
        return session.query(exists().where(User.id == user_id)).scalar()

    def get_user_by_id(self, session: Session, user_id):
        '''Find a user by their id, if it exists'''
        return (session.query(User)
                .filter_by(id=user_id)
                .one_or_none())

    # chat methods
    def get_chat_by_id(self, session: Session, chat_id):
        '''Find a chat by its id, if it exists'''
        return (session.query(Chat)
                .filter_by(id=chat_id)
                .one_or_none())

    # quote methods
    def get_quote_by_id(self, session: Session, quote_id):
        '''Find a quote by its id, if it exists'''
        return (session.query(Quote)
                .filter_by(id=quote_id)
                .one_or_none())

    def add_quote(
            self, session: Session, chat_id, message_id, is_forward, forwarded_by_id, forwarded_at, sent_by_id,
            sent_at, message_type, content, content_html, file_id, quoted_by_id, quoted_at):
        '''Insert a new quote into the database'''

        # check if quote already exists
        quote = (session.query(Quote.id, Quote.deleted)
                        .filter_by(
                            sent_at=sent_at,
                            sent_by_id=sent_by_id,
                            chat_id=chat_id,
                            content_html=content_html)
                        .one_or_none())

        if quote is not None:
            quote_id, deleted = quote

            if deleted:
                return None, self.QUOTE_PREVIOUSLY_DELETED

            return self.get_quote_by_id(quote_id), self.QUOTE_ALREADY_EXISTS

        # find chat and relevant user objects
        chat = self.get_chat_by_id(chat_id)
        sent_by = self.get_user_by_id(sent_by_id)
        quoted_by = self.get_user_by_id(quoted_by_id)
        forwarded_by = self.get_user_by_id(forwarded_by_id)

        # add quote to the database
        quote = Quote(
            chat=chat, message_id=message_id, is_forward=is_forward, forwarded_by=forwarded_by,
            forwarded_at=forwarded_at, sent_by=sent_by, sent_at=sent_at, message_type=message_type,
            content=content, content_html=content_html, file_id=file_id, quoted_by=quoted_by,
            quoted_at=quoted_at)

    # quote message methods

    # vote methods
