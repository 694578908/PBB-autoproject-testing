import pytest

from common.log_set import clear_logs
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
    return data


# 存放环境url地址
@pytest.fixture(scope="session", autouse=True)
def write_url_yaml():
    login_url = read_config_ini()['url']['app_url']
    module_url = read_config_ini()['url']['ht_url']
    url = {'app_url': login_url, 'ht_url': module_url}
    YamlUtil().write_extract_yaml(url)


# 读取MySQL配置账号
@pytest.fixture(scope="session", autouse=True)
def read_mysql_account():
    host = read_config_ini()['mysql']['host']
    user = read_config_ini()['mysql']['user']
    password = read_config_ini()['mysql']['password']
    database = read_config_ini()['mysql']['database']
    data = (host, user, password, database)
    return data


# 实时清除extract.yml
@pytest.fixture(scope="session", autouse=True)
def clear_extract_yaml():
    YamlUtil().clear_extract_yaml()
    yield


# 定时清除log日志
@pytest.fixture(scope="session", autouse=True)
def clear_log():
    # 设置过期时间（以小时为单位）
    expiration_hours = int(read_config_ini()['log']['expiration_hours'])
    clear_logs(expiration_hours)
    yield
