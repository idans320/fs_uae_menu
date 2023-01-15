from cgitb import enable
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from .base import Base
from .game_image import GameImage


class Game(Base):
    __tablename__ = "games"
    name = Column(String, primary_key=True)
    directory_name = Column(String, primary_key=False)
    images = relationship("GameImage", order_by=GameImage.path, back_populates="game")
    enabled = Column(Boolean, default=False)

    def __init__(self, name: str, directory_name: str, enabled: bool):
        self.name = name.title()
        self.enabled = enabled
        self.directory_name = directory_name
