import pytest

from common.read_write_yaml import YamlUtil
from common.readfile_config_path import read_config_ini


# redis参数配置项
@pytest.fixture(scope='session')
def read_config_redis_data():
    host = read_config_ini()['redis']['host']
    password = read_config_ini()['redis']['password']
    port = read_config_ini()['redis']['port']
    db = read_config_ini()['redis']['db']
    key = read_config_ini()['redis']['key']  # 需要自定义修改想要获取手机验证码
    data = (host, password, port, db, key)
    print(host, password, port, db, key)
    return data


# 实时清除extract.yml
@pytest.fixture(scope="session", autouse=True)
def clear_extract_yaml():
    YamlUtil().clear_extract_yaml()
    yield
