import json

import allure


def testcase_allure_title(name):
    allure.dynamic.title(name)


def testcase_allure_attach(max_timeout, elapsed_time_rounded, method, url, headers, rep, data):
    timeout_message = f'接口限制最大请求时间: {max_timeout}, 接口实际请求时间: {elapsed_time_rounded}'
    response_url = f'method:{method}, url: {url}'
    allure.attach(json.dumps(timeout_message, ensure_ascii=False, indent=2), name="接口响应时间",
                  attachment_type=allure.attachment_type.JSON)
    allure.attach(json.dumps(response_url, ensure_ascii=False, indent=2), name="请求地址",
                  attachment_type=allure.attachment_type.JSON)
    allure.attach(json.dumps(headers, ensure_ascii=False, indent=2), name="请求头",
                  attachment_type=allure.attachment_type.JSON)
    allure.attach(json.dumps(data, ensure_ascii=False, indent=2), name="请求数据",
                  attachment_type=allure.attachment_type.JSON)
    allure.attach(json.dumps(rep.json(), ensure_ascii=False, indent=2), name="接口响应",
                  attachment_type=allure.attachment_type.JSON)


def allure_success_message(key, validate_value, actual_value, res):
    log_status = f'用例断言成功：预期{key}:{validate_value},实际{key}:{actual_value}'
    allure.attach(f'预期{key}:{validate_value},实际{res}', name=log_status)


def allure_validate_message():
    log_status = '用例断言失败'
    allure.attach(f"yaml用例validate字段为必填，不能为空", name=log_status)


def allure_None_message(key, error_messages):
    log_status = '用例断言失败'
    expected_value_message = f" yaml用例validate.{key}的值为必填，不能为空"
    error_messages.append(expected_value_message)
    allure.attach(f" yaml用例validate.{key}的值为必填，不能为空", name=log_status)


def allure_validate_value_message(key, error_messages, res):
    log_status = f'用例断言失败:validate的key：{key}'
    validate_value_message = f" 用例断言失败：yaml用例validate里填写的：{key},与接口实际返回的{res}不一致"
    error_messages.append(validate_value_message)
    allure.attach(validate_value_message, name=log_status)


def allure_error_message(key, validate_value, error_messages, actual_value):
    log_status = '用例断言失败'
    actual_value_message = f" 期望 {key}:{validate_value},但实际为{key}:{actual_value}"
    error_messages.append(actual_value_message)
    allure.attach(actual_value_message, name=log_status)
