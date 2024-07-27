import allure
import pytest
from common.read_write_yaml import YamlUtil
from common.testcase_request_response import case_request


#     @allure.feature('C端')
#     @pytest.mark.parametrize('case', YamlUtil().read_testcase_login_data('C_module.yml', 'C_module'))
#     def test_case_C_module(self, case):
#         case_request(case)
#
#     @allure.feature('B端')
#     @pytest.mark.parametrize('case', YamlUtil().read_testcase_login_data('B_module.yml', 'B_module'))
#     def test_case_B_module(self, case):
#         case_request(case)
@allure.epic('APP-C端-接口功能模块')
class TestCmodule:
    @pytest.mark.parametrize('case', YamlUtil().read_testcase_dir('testcases_C_data'))
    def test_case_C_module(self, case):
        case_request(case)


@allure.epic('APP-B端-接口功能模块')
class TestBmodule:
    @pytest.mark.parametrize('case', YamlUtil().read_testcase_dir('testcases_B_data'))
    def test_case_B_module(self, case):
        case_request(case)

    # @allure.feature('后台-Web端')
    # @pytest.mark.parametrize('case', YamlUtil().read_testcase_dir('testcases_HT_data'))
    # def test_case_B_module(self, case):
    #     case_request(case)
