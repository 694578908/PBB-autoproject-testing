import allure
import pytest

from common.read_write_yaml import YamlUtil
from testcases.testcase_request_response import case_request


@allure.epic('PBB')
class TestRequest:
    @allure.feature('登录功能模块')
    @pytest.mark.parametrize('case', YamlUtil().read_testcase_yaml('test_case.yml', 'login'))
    def test_case_login(self, case):
        res = case_request(case)


# 登录账号密码

if __name__ == '__main__':
    pytest.main()
