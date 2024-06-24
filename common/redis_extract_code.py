import redis
import pytest

from common.read_write_yaml import YamlUtil
from common.testcase_allure_reports import allure_redis_timeout, allure_redis_unresponsive, allure_redis_codeerror


def read_redis(read_config_redis_data):
    host, password, port, db, key = read_config_redis_data
    try:
        redis_client = redis.StrictRedis(host=host, port=port, password=password, db=db, decode_responses=True)
        response = redis_client.ping()
        if response:
            folder_key = 'pbb_applet_user_login_code:'
            full_key = folder_key + key
            full_key_value = redis_client.get(full_key)
            if full_key_value is None:
                pytest.fail(allure_redis_codeerror(full_key, full_key_value))
            value = full_key_value.strip('""')
            data = {'code': value}
            YamlUtil().write_extract_yaml(data)
        else:
            pytest.fail(allure_redis_unresponsive())
        redis_client.close()
    except redis.exceptions.ConnectionError:
        pytest.fail(allure_redis_timeout())
