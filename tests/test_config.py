from atari_menu.config import Config
from pytest_mock import MockerFixture
from unittest.mock import mock_open

def test_db_url_default(mocker : MockerFixture):
    mocker.patch("atari_menu.config.ConfigType._yml",new={})
    assert Config.db_url == "sqlite://"


def test_db_url_yml(mocker : MockerFixture):
    test_db_yml = '''
        db:
            connection_string: sqlite://test
    '''
    mocker.patch("builtins.open", mock_open(read_data=test_db_yml))
    assert Config.db_url == "sqlite://test"