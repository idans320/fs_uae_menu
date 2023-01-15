from pyexpat import model
from atari_menu.db import get_session
from atari_menu.models import Game
from sqlalchemy.sql import func
from typing import List
from atari_menu.config import Config
from pathlib import Path

FS_UAE_CONFIG = '''cpu_speed=max
cpu_throttle=30000.0
cpu_type=68040
accuracy = -1
amiga_model = A1000
graphics_card = uaegfx-z3
'''

class GameInterface:
    @staticmethod
    def get_games_by_first_character_range(f, l) -> List[Game]:
        with get_session() as session:
            models = (
                session.query(Game).where(
                    func.substr(Game.name, 1, 1) >= f
                    ,func.substr(Game.name, 1, 1) < l
                )
            ).all()
            session.expunge_all()
            return models

    @staticmethod
    def get_all_enabled_games() -> List[Game]:
        with get_session() as session:
            models = (
                session.query(Game).where(
                    Game.enabled == 1
                )
            ).all()
            session.expunge_all()
            return models
            
    @staticmethod
    def save_selection_to_db(enabled : List[Game], disabled : List[Game]):
        with get_session() as session:
            for game in enabled:
                game.enabled = True
                session.add(game)
            for game in disabled:
                game.enabled = False
                session.add(game)
            
    @staticmethod
    def save_selection_to_config_file():
        with get_session() as session:
            games : List[Game] = (
                session.query(Game).where(
                    Game.enabled == 1
                )
            ).all()
            config_file : str = Config.floppy_file
            with open(config_file,'w') as f:
                f.write(FS_UAE_CONFIG)
                for index, game in enumerate(games):
                    for image in game.images:
                        game_path = str(Path(game.directory_name) / image.path)
                        f.write(f"floppy_image_{index}={game_path}\n")
