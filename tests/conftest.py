import pytest
from sqlalchemy import create_engine
from atari_menu.db import get_session
from atari_menu.models.base import Base

@pytest.fixture()
def db_session():
    engine = create_engine("sqlite://")
    Base.metadata.bind = engine
    Base.metadata.create_all()
    with get_session(engine) as session:
        yield session
        session.close()
    Base.metadata.drop_all()
