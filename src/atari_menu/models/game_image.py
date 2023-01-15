from sqlalchemy import Column, ForeignKey, String, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from .base import Base

class GameImage(Base):
    __tablename__ = 'game_images'
    game_name = Column(String, ForeignKey('games.name'))
    game = relationship("Game", back_populates="images")
    path = Column(String, primary_key=True)
    def __init__(self,path,game_name):
        self.path = path
        self.game_name = game_name.title()