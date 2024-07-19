import allure
import requests
import time
import json
import pytest

from common.testcase_allure_reports import testcase_allure_attach, allure_requesttime_success, allure_requesttime_fail, \
    requests_exceptions_ProxyError, requests_exceptions_RequestException, request_timeout_message, request_NONE_message


class RequestUtil:
    session = requests.session()

    # 发送请求
    def send_request_util(self, title, headers, url, data, method, max_timeout=5, proxies=None, **kwargs):
        method = str(method).lower()
        start_time = time.time()
        rep = None
        request_data = data
        try:
            if method == 'get':
                rep = RequestUtil.session.request(method=method, url=url, params=data, headers=headers,
                                                  timeout=max_timeout, proxies=proxies, **kwargs)
            else:
                res_data = json.dumps(request_data)
                rep = RequestUtil.session.request(method=method, url=url, data=res_data, headers=headers,
                                                  timeout=max_timeout, **kwargs)

        except requests.Timeout:
            end_time = time.time()
            elapsed_time = end_time - start_time
            elapsed_time_rounded = round(elapsed_time, 2)
            request_timeout_message(max_timeout, elapsed_time_rounded)

        except requests.exceptions.ProxyError as e:
            requests_exceptions_ProxyError(e)

        except requests.RequestException as e:
            requests_exceptions_RequestException(e)

        try:
            end_time = time.time()
            elapsed_time = end_time - start_time
            elapsed_time_rounded = round(elapsed_time, 2)
            if rep:
                testcase_allure_attach(title, max_timeout, elapsed_time_rounded, rep.request.method, rep.url, headers, rep,
                                       request_data)

                assert rep.status_code == 200
                allure_requesttime_success(rep.status_code)
                return rep.text
            else:
                request_timeout_message(max_timeout, elapsed_time_rounded)
                pytest.fail(request_NONE_message())1
        except AssertionError as e:

            pytest.fail(allure_requesttime_fail(e, rep.status_code))


