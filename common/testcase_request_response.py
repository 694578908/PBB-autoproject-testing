import json
import jsonpath
import pytest

from common.read_write_yaml import YamlUtil
from common.regular_expression_method import regular_expression_extract
from common.request_util import RequestUtil
from common.testcase_allure_reports import testcase_allure_title, jsonpath_case_message, case_key_message, \
    extract_key_message, extract_value_message, storage_value_messgae, storage_key_messgae
from common.testcase_assertion_results import assert_validate_response
from common.testcase_counter import count
from common.variable_correlation_method import readextract_and_replacevariables


def case_request(case):
    count(case)
    if 'name' in case.keys() and 'requests' in case.keys() and 'validate' in case.keys():
        if jsonpath.jsonpath(case, '$..url') and jsonpath.jsonpath(case, '$..method') \
                and jsonpath.jsonpath(case, '$..data') and jsonpath.jsonpath(case, '$..headers'):
            testcase_allure_title(case['name'])
            replace = readextract_and_replacevariables(case)
            # 判断replace.extract字段是否为空
            if 'storage' in replace:
                if replace['storage'] is None:
                    pytest.fail(storage_key_messgae())
                else:
                    for storage_key, storage_value in replace['storage'].items():
                        if storage_value is None:
                            pytest.fail(storage_value_messgae(storage_key, storage_value))
                        else:
                            storage_dict = replace['storage']
                            YamlUtil().write_extract_yaml(storage_dict)
            title = case['name']
            headers = case['requests']['headers']
            url = case['requests']['url']
            data = case['requests']['data']
            method = case['requests']['method']
            request_result = RequestUtil().send_request_util(title, headers, url, data, method)
            res = json.loads(request_result)
            # 判断replace.extract字段是否为空
            if 'extract' in replace:
                if replace['extract'] is None:
                    pytest.fail(extract_key_message())
                else:
                    for extract_key, extract_value in replace['extract'].items():
                        if extract_value is None:
                            pytest.fail(extract_value_message(extract_key, extract_value))
                        else:
                            extract_value = replace['extract']
                            regular_expression_extract(extract_value, request_result)
            # 判断replace.validate是否为空并且与res返回结果做对比
            assert_validate_response(replace, res)
            return url
        else:
            pytest.fail(jsonpath_case_message())
    else:
        pytest.fail(case_key_message())
