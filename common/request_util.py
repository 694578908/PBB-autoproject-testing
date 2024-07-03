import allure
import requests
import time
import json
import pytest

from common.testcase_allure_reports import testcase_allure_attach, allure_requesttime_success, allure_requesttime_fail


class RequestUtil:
    session = requests.session()

    # 发送请求
    def send_request_util(self, title, headers, url, data, method, max_timeout=5, **kwargs):
        method = str(method).lower()
        start_time = time.time()
        rep = None
        request_data = data
        try:
            if method == 'get':
                rep = RequestUtil.session.request(method=method, url=url, params=data, headers=headers,
                                                  timeout=max_timeout, **kwargs)
            else:
                res_data = json.dumps(request_data)
                rep = RequestUtil.session.request(method=method, url=url, data=res_data, headers=headers,
                                                  timeout=max_timeout, **kwargs)

        except requests.Timeout:
            end_time = time.time()
            elapsed_time = end_time - start_time
            elapsed_time_rounded = round(elapsed_time, 2)
            timeout_message = {'接口限制最大请求时间': max_timeout, '接口实际请求时间': elapsed_time_rounded}
            pytest.fail(f"接口超时: {timeout_message}")
            return

        end_time = time.time()
        elapsed_time = end_time - start_time
        elapsed_time_rounded = round(elapsed_time, 2)

        testcase_allure_attach(title, max_timeout, elapsed_time_rounded, rep.request.method, rep.url, headers, rep,
                               request_data)

        try:
            assert rep.status_code == 200
            allure_requesttime_success(rep.status_code)
        except AssertionError as e:
            pytest.fail(allure_requesttime_fail(e, rep.status_code))

        return rep.text
