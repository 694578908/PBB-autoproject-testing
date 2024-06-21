import jsonpath
import pytest


def assert_validate_response(replace, res):
    validate = replace['validate']
    if validate is None:
        validate_message = f"用例validate字段为必填，不能为空"
        pytest.fail(validate_message)
    else:
        for key, expected_value in validate.items():
            actual_value = jsonpath.jsonpath(res, f'$..{key}')
            if actual_value is False:
                error_message = f"断言失败：yaml用例validate里填写的：{key},与接口实际返回的{res}不一致"
                pytest.fail(error_message)
            else:
                if not actual_value or actual_value[0] != expected_value:
                    error_message = f"断言失败: 期望 {key}:{expected_value},但实际为{key}:{actual_value}"
                    pytest.fail(error_message)
                print(f"断言成功: 预期{key}:{expected_value} 实际{key}:{actual_value}")
        return True
