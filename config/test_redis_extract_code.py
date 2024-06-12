import redis
import pytest

from common.read_write_yaml import YamlUtil


def test_read_redis(read_config_redis_data):
    host, password, port, db, key = read_config_redis_data
    redis_client = redis.StrictRedis(host=host, port=port, password=password, db=db, decode_responses=True)
    response = redis_client.ping()
    if response:
        folder_key = 'pbb_applet_user_login_code:'
        full_key = folder_key + key
        value = redis_client.get(full_key)
        if value is None:
            error_message = "未获取到验证码，请检查手机号输入是否正确（手机号切勿设置白名单）"
            pytest.fail(error_message)
        data = {'code': value}
        YamlUtil().write_extract_yaml(data)
    else:
        error_message = "Redis连接超时，请检查连接配置和网络是否正常"
        pytest.fail(error_message)

    redis_client.close()


if __name__ == '__main__':
    pytest.main()
