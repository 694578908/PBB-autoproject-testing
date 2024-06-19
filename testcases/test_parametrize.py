import allure
import pytest

from common.read_write_yaml import YamlUtil
from common.redis_extract_code import test_read_redis
from testcases.testcase_request_response import case_request


# 登录账号密码
@allure.epic('PBB')
class TestRequest:
    @allure.feature('登录功能模块')
    @pytest.mark.parametrize('case', YamlUtil().read_testcase_yaml('test_case.yml', 'login'))
    def test_case_login(self, case, read_config_redis_data):
        host, password, port, db, key = read_config_redis_data
        res = case_request(case)
        if key in res:
            test_read_redis(read_config_redis_data)


if __name__ == '__main__':
    pytest.main()
