import redis
import pytest

from common.read_write_yaml import YamlUtil


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
                error_message = "未获取到验证码，请检查手机号输入是否正确（手机号切勿设置白名单）"
                pytest.fail(error_message)
            value = full_key_value.strip('""')
            data = {'code': value}
            YamlUtil().write_extract_yaml(data)
        else:
            error_message = "Redis已连接但没有响应"
            pytest.fail(error_message)
        redis_client.close()
    except redis.exceptions.ConnectionError:
        timeout_error_message = "Redis连接超时，请检查连接配置和网络是否正常"
        pytest.fail(timeout_error_message)


