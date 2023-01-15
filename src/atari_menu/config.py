from dataclasses import dataclass
from distutils.file_util import copy_file
from typing import Any, Dict
import yaml
from yaml import SafeLoader
from atari_menu.utils.paths import relative_root_project
import pydash  as py_

class ConfigKey:
    default = None
    path : str
    def __init__(self,path,default=None):
        self.default = default
        self.path = path

class ConfigType:
    @property
    def _yml(self) -> Dict[str,any]:
        with open(relative_root_project("config.yml")) as f:
            data = yaml.load(f, Loader=SafeLoader)
        return data
    def  __getattribute__(self, attr: str) -> Any:
        if isinstance(key :=super().__getattribute__(attr), ConfigKey):
            defined_key = py_.get(self._yml,key.path)
            if defined_key:
                return defined_key
            else:
                return key.default
        return super().__getattribute__(attr)

class _Config(ConfigType):
    db_url : str = ConfigKey(default="sqlite://",path="db.connection_string")
    floppy_file : str = ConfigKey(path="files.floppy")
    cmd : str = ConfigKey(path="exec")
Config = _Config()