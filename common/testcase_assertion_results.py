import jsonpath
import pytest


def validate_response(validate, res):
    for key, expected_value in validate.items():
        actual_value = jsonpath.jsonpath(res, f'$..{key}')
        if not actual_value or actual_value[0] != expected_value:
            error_message = f"断言失败: 期望 {key} 为 {expected_value}, 但实际为 {actual_value}"
            pytest.fail(error_message)
        print("断言成功")
    return True
