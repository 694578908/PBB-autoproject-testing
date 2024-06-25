import allure
import pytest

from common.read_write_yaml import YamlUtil
from common.redis_extract_code import read_redis

from common.testcase_request_response import case_request


@allure.epic('PBB-聘播播接口自动化测试')
class TestRequest:
    # PBB-聘播播客户端账号密码登录
    # @allure.feature('PBB-聘播播客户端登录功能模块')
    # @pytest.mark.parametrize('case', YamlUtil().read_testcase_yaml('test_case.yml', 'PBB_login'))
    # def test_case_login(self, case, read_config_redis_data):
    #     res = case_request(case)
    #     host, password, port, db, key = read_config_redis_data
    #     if key in res:
    #         read_redis(read_config_redis_data)

    @allure.feature('PBB-聘播播后台管理登录功能模块')
    @pytest.mark.parametrize('case', YamlUtil().read_testcase_yaml('test_case.yml', 'PBB_backstage_login'))
    def test_case_backstage_login(self, case):
        res = case_request(case)
