import allure
import pytest

from common.read_write_yaml import YamlUtil
from common.redis_extract_code import read_redis

from common.testcase_request_response import case_request


@allure.epic('聘播播-客户端自动化测试')
class TestClient:
    @allure.feature('客户端-用户登陆')
    @pytest.mark.parametrize('case', YamlUtil().read_testcase_yaml('PBB_app_login.yml', 'PBB_app_login'))
    def test_case_login(self, case, read_config_redis_data):
        res = case_request(case)
        host, password, port, db, key = read_config_redis_data
        if key in res:
            read_redis(read_config_redis_data)

    @allure.feature('C端')
    @pytest.mark.parametrize('case', YamlUtil().read_testcase_yaml('C_module.yml', 'C_module'))
    def test_case_C_module(self, case):
        case_request(case)

    @allure.feature('B端')
    @pytest.mark.parametrize('case', YamlUtil().read_testcase_yaml('B_module.yml', 'B_module'))
    def test_case_B_module(self, case):
        case_request(case)


@allure.epic('聘播播-后台管理自动化测试')
class TestBackground:
    @allure.feature('后台管理')
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.parametrize('case', YamlUtil().read_testcase_yaml('PBB_backstage_login.yml', 'PBB_backstage_login'))
    def test_case_backstage_login(self, case):
        case_request(case)
