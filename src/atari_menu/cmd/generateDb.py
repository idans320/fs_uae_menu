from pathlib import Path
from typing import Union
from os import walk
from atari_menu.db import get_session, get_default_engine
from atari_menu.models import Game
from atari_menu.models import GameImage
from atari_menu.models.base import Base


def generate_index_by_folder(folder: str):
    for dirpath, dirnames, _ in walk(folder):
        for dirname in dirnames:
            game_dir = Path(dirpath) / dirname
            for _, _, filenames in walk(game_dir):
                for filename in filenames:
                    yield (dirname, f"{dirname}/", filename)


def run(path):
    games = set()
    filenames = set()

    Base.metadata.bind = get_default_engine()
    Base.metadata.create_all()
    for entry in generate_index_by_folder(path):
        with get_session() as session:
            game_name, dir_name, game_image = entry
            if not game_name in games:
                game = Game(name=game_name, directory_name=dir_name, enabled=False)
                games.add(game_name)
                session.add(game)
                session.commit()

        if not game_image in filenames:
            gameimg = GameImage(
                path=game_image, game_name=game_name
            )
            filenames.add(game_image)
            session.add(gameimg)
            session.commit()