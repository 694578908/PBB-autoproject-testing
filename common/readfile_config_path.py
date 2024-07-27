import configparser
import os
from common.testcase_allure_reports import dir_None_massage


def read_config_ini(path="./config/config.ini"):
    abs_path = os.path.abspath(path)
    if os.path.isfile(abs_path):
        config = configparser.ConfigParser()
        config.read(abs_path, encoding='utf-8-sig')
        return config
    else:
        raise FileNotFoundError(dir_None_massage(abs_path))
