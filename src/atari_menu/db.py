from sqlalchemy import create_engine
from atari_menu.config import Config
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager
from typing import Generator

def get_default_engine():
    return create_engine(Config.db_url)

@contextmanager
def get_session(engine = None) -> Generator[Session,None,None]:
    if not engine:
        engine = get_default_engine()
    Session  = sessionmaker(engine)
    with Session() as session:
        yield session
        session.commit()