import requests
import time
import json
import pytest


class RequestUtil:
    session = requests.session()

    # 发送请求
    def send_request_util(self, method, url, data, headers, timeout_value=5, **kwargs):
        method = str(method).lower()
        start_time = time.time()
        rep = None

        try:
            if method == 'get':
                rep = RequestUtil.session.request(method=method, url=url, params=data, headers=headers,
                                                  timeout=timeout_value, **kwargs)
            else:
                data = json.dumps(data)
                rep = RequestUtil.session.request(method=method, url=url, data=data, headers=headers,
                                                  timeout=timeout_value, **kwargs)
        except requests.Timeout:
            end_time = time.time()
            elapsed_time = end_time - start_time
            elapsed_time_rounded = round(elapsed_time, 2)
            timeout_message = {'接口限制最大请求时间': timeout_value, '接口实际请求时间': elapsed_time_rounded}
            pytest.fail(f"接口超时: {timeout_message}")
            return

        end_time = time.time()
        elapsed_time = end_time - start_time
        elapsed_time_rounded = round(elapsed_time, 2)
        timeout_message = {'接口限制最大请求时间': timeout_value, '接口实际请求时间': elapsed_time_rounded}

        try:
            assert rep.status_code == 200
            code_message = f'接口响应成功, 请求耗时: {elapsed_time_rounded} 秒'
        except AssertionError:
            code_message = f'接口响应失败, 请求耗时: {elapsed_time_rounded} 秒'
            pytest.fail(code_message)

        return rep.text
