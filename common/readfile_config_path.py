import configparser
import os


def read_config_ini(path="/pbb-autoproject-testing/config/config.ini"):
    abs_path = os.path.abspath(path)
    config = configparser.ConfigParser()
    config.read(abs_path, encoding='utf-8-sig')
    return config
