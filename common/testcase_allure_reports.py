import json

import allure

from common.log_set import log


# testcase_request_response.py：标题
def testcase_allure_title(name):
    allure.dynamic.title(name)


def storage_key_messgae():
    log_status = f"yaml用例storage目录下字段key为必填，不能为空，如不需要storage可以直接删除"
    log.error(log_status)
    allure.attach(log_status, name=log_status)


def storage_value_messgae(storage_key, storage_value):
    log_status = f'yaml用例storage目录下{storage_key}：{storage_value}值应必填，不能为空'
    log.error(log_status)
    allure.attach(name=log_status)


def extract_key_message():
    log_status = f"yaml用例extract目录下字段key为必填，不能为空，如不需要extract可以直接删除"
    log.error(log_status)
    allure.attach(name=log_status)


def extract_value_message(extract_key, extract_value):
    log_status = f'yaml用例extract目录下{extract_key}：{extract_value}值应为正则表达式，不能为空'
    log.error(log_status)
    allure.attach(name=log_status)


def jsonpath_case_message():
    log_status = '在yml文件requests目录下必须要有method,url,data,headers'
    log.error(log_status)
    allure.attach(name=log_status)


def case_key_message():
    log_status = 'yml一级关键字必须包含:name,requests,validate'
    log.error(log_status)
    allure.attach(name=log_status)


# testcase_allure_reports.py：接口请求响应等参数的消息
def testcase_allure_attach(title, max_timeout, elapsed_time_rounded, method, url, headers, rep, data):
    timeout_message = f'接口限制最大请求时间: {max_timeout}, 接口实际请求时间: {elapsed_time_rounded}'
    response_url = f'method:{method}, url: {url}'
    allure.attach(json.dumps(timeout_message, ensure_ascii=False, indent=2), name="接口响应时间",
                  attachment_type=allure.attachment_type.JSON)
    allure.attach(json.dumps(response_url, ensure_ascii=False, indent=2), name="请求地址",
                  attachment_type=allure.attachment_type.JSON)
    allure.attach(json.dumps(headers, ensure_ascii=False, indent=2), name="请求头",
                  attachment_type=allure.attachment_type.JSON)
    allure.attach(json.dumps(data, ensure_ascii=False, indent=2), name="请求参数",
                  attachment_type=allure.attachment_type.JSON)
    allure.attach(json.dumps(rep.json(), ensure_ascii=False, indent=2), name="接口响应",
                  attachment_type=allure.attachment_type.JSON)
    log.info('响应时间:{}'.format(timeout_message))
    log.info('用例标题:{}'.format(title))
    log.info('请求地址:{},请求头:{}'.format(response_url, headers))
    log.info('请求参数:{}'.format(data))
    log.info('接口返回信息为:{}'.format(rep.json()))


# testcase_assertion_results.py：参数返回与yaml预期对比消息体
def allure_success_message(key, validate_value, actual_value, res):
    log_status = f'用例断言成功：预期{key}:{validate_value},实际{key}:{actual_value}'
    allure.attach(f'预期{key}:{validate_value},实际{res}', name=log_status)
    log.info(log_status)


def allure_validate_message(validate):
    log_status = '用例断言失败'
    allure.attach(f"yaml用例{validate}字段为必填，不能为空", name=log_status)
    log.error(f'用例断言失败: yaml用例{validate}字段为必填，不能为空')


def allure_None_message(key, error_messages):
    log_status = '用例断言失败'
    expected_value_message = f" yaml用例validate.{key}的值为必填，不能为空"
    error_messages.append(expected_value_message)
    allure.attach(f" yaml用例validate.{key}的值为必填，不能为空", name=log_status)
    log.error(f"{log_status}:{expected_value_message}")


def allure_validate_value_message(key, error_messages, res):
    log_status = f'用例断言失败:validate的key：{key}'
    validate_value_message = f" 用例断言失败：yaml用例validate里填写的：{key},与接口实际返回的{res}不一致"
    error_messages.append(validate_value_message)
    allure.attach(validate_value_message, name=log_status)
    log.error(f"{log_status}:{validate_value_message}")


def allure_error_message(key, validate_value, error_messages, actual_value):
    log_status = "用例断言失败"
    actual_value_message = f" 期望 {key}:{validate_value},但实际为{key}:{actual_value}"
    error_messages.append(actual_value_message)
    allure.attach(actual_value_message, name=log_status)
    log.error(f"{log_status}:{actual_value_message}")


# request_util.py:接口响应消息
def allure_requesttime_success(status_code):
    log_status = f'接口响应成功code:{status_code}'
    code_message = f"code:{status_code}"
    allure.attach(code_message, name=log_status)
    log.info(f"{log_status}:{code_message}")


def allure_requesttime_fail(status_code):
    log_status = f'接口响应失败code:{status_code}'
    code_message = f"code:{status_code}"
    allure.attach(code_message, name=log_status)
    log.error(f"{log_status}:{code_message}")


# redis_extract_code.py：redis响应消息
def allure_redis_codeerror(full_key, full_key_value):
    log_status = "未获取到验证码，请检查手机号输入是否正确（手机号切勿设置白名单）"
    code_message = f"{full_key}:{full_key_value}"
    allure.attach(code_message, name=log_status)
    log.error(f"{log_status}:{code_message}")


def allure_redis_unresponsive():
    log_status = "Redis已连接但没有响应"
    log.info(log_status)
    allure.attach(name=log_status)
    log.error(f"{log_status}")


def allure_redis_timeout():
    log_status = "Redis连接超时，请检查连接配置和网络是否正常"
    allure.attach(name=log_status)
    log.error(f"{log_status}")
