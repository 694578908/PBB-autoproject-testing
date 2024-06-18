import json

import allure
import jsonpath
import pytest

from common.request_util import RequestUtil


def test_case_request(case):
    if 'name' in case.keys() and 'requests' in case.keys() and 'validate' in case.keys():
        if jsonpath.jsonpath(case, '$..url') and jsonpath.jsonpath(case, '$..method') \
                and jsonpath.jsonpath(case, '$..data') and jsonpath.jsonpath(case, '$..headers'):
            allure.dynamic.title(case['name'])
            title = case['name']
            headers = case['headers']
            url = case['url']
            data = case['data']
            method = case['method']
            request_result = RequestUtil.send_request_util(title, headers, url, data, method)
            res = json.loads(request_result)
        else:
            jsonpath_case_message = '在yml文件requests目录下必须要有method,url,data,headers'
            pytest.fail(jsonpath_case_message)
    else:
        case_key_message = 'yml一级关键字必须包含:name,requests,validate'
        pytest.fail(case_key_message)




