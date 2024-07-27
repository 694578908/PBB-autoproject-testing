import allure
import pytest

from common.read_write_yaml import YamlUtil
from common.redis_extract_code import read_redis
from common.testcase_request_response import case_request


@allure.epic('聘播播-登录功能测试')
class TestLogin:
    @allure.feature('客户端-用户登陆')
    @pytest.mark.parametrize('case', YamlUtil().read_testcase_login_data('PBB_app_login.yml', 'PBB_app_login'))
    def test_case_login(self, case, read_config_redis_data):
        res = case_request(case)
        host, password, port, db, key = read_config_redis_data
        if key in res:
            read_redis(read_config_redis_data)

    @allure.feature('后台管理-登录')
    # @pytest.mark.flaky(reruns=3, rerun_delay=1)
    @pytest.mark.parametrize('case', YamlUtil().read_testcase_login_data('PBB_backstage_login.yml', 'PBB_backstage_login'))
    def test_case_backstage_login(self, case):
        case_request(case)
