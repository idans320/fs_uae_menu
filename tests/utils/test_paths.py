import pathlib
from atari_menu.utils.paths import relative_root_project

def test_root_project_path():
   path = relative_root_project("config.yml")
   assert path.find("src") == -1