from cgitb import enable
from sqlalchemy.orm import Session
from atari_menu.models.game import Game
from atari_menu.models.game_image import GameImage

def test_create_models(db_session : Session):
    game = Game(name="SimCity", directory_name="/", enabled=True)
    db_session.add(game)
    db_session.commit()

    game_image = GameImage(game_name="SimCity",path="/")
    db_session.add(game_image)
    db_session.commit()