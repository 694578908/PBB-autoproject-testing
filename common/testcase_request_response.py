import json

import allure
import jsonpath
import pytest

from common.read_write_yaml import YamlUtil
from common.regular_expression_method import regular_expression_extract
from common.request_util import RequestUtil
from common.testcase_assertion_results import assert_validate_response
from common.testcase_counter import count
from common.variable_correlation_method import readextract_and_replacevariables


def case_request(case):
    count(case)
    if 'name' in case.keys() and 'requests' in case.keys() and 'validate' in case.keys():
        if jsonpath.jsonpath(case, '$..url') and jsonpath.jsonpath(case, '$..method') \
                and jsonpath.jsonpath(case, '$..data') and jsonpath.jsonpath(case, '$..headers'):
            allure.dynamic.title(case['name'])
            replace = readextract_and_replacevariables(case)
            if 'storage' in replace:
                if replace['storage'] is None:
                    storage_messgae = f"用例storage字段必填，不能为空，如不需要storage可以直接删除"
                    pytest.fail(storage_messgae)
                else:
                    storage_value = replace['storage']
                    YamlUtil().write_extract_yaml(storage_value)
            title = case['name']
            headers = case['requests']['headers']
            url = case['requests']['url']
            data = case['requests']['data']
            method = case['requests']['method']
            request_result = RequestUtil().send_request_util(title, headers, url, data, method)
            res = json.loads(request_result)
            if 'extract' in replace:
                if replace['extract'] is None:
                    extract_message = f"用例extract字段必填，不能为空，如不需要extract可以直接删除"
                    pytest.fail(extract_message)
                else:
                    extract_value = replace['extract']
                    regular_expression_extract(extract_value, request_result)
            assert_validate_response(replace, res)
            return url

        else:
            jsonpath_case_message = '在yml文件requests目录下必须要有method,url,data,headers'
            pytest.fail(jsonpath_case_message)

    else:
        case_key_message = 'yml一级关键字必须包含:name,requests,validate'
        pytest.fail(case_key_message)
