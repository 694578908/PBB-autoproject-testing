import jsonpath
import pytest

from common.testcase_allure_reports import allure_error_message, allure_success_message, allure_validate_value_message, \
    allure_None_message, allure_validate_message


def assert_validate_response(replace, res):
    validate = replace['validate']
    if validate is None:
        pytest.fail(allure_validate_message())
    else:
        error_messages = []
        for key, validate_value in validate.items():
            if validate_value is None:
                allure_None_message(key, error_messages)
            else:
                actual_value = jsonpath.jsonpath(res, f'$..{key}')
                if actual_value is False:
                    allure_validate_value_message(key, error_messages, res)
                else:
                    if not actual_value or actual_value[0] != validate_value:
                        allure_error_message(key, validate_value, error_messages, actual_value)
                    else:
                        allure_success_message(key, validate_value, actual_value, res)
        if error_messages:
            pytest.fail('\n'.join(error_messages))

        return True
