'''Miscellanious utility methods'''

import functools
import logging
from main import quote_database


def session_scope():
    '''Define a session scope for database transactions'''
    session = quote_database.create_session()

    try:
        yield session
        session.commit()
    except Exception as e:
        logging.ERROR(e)
        session.rollback()
        raise
    finally:
        session.close()


def with_session(f):
    '''Wrapper decorative to pass a session object to database methods'''
    @functools.wraps(f)
    def with_session(*args, **kwargs):
        with session_scope() as session:
            kwargs.update(session=session)
            return f(*args, **kwargs)

    return with_session
