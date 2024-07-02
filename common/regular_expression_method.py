import re

import pytest

from common.read_write_yaml import YamlUtil
from common.testcase_allure_reports import allure_regular_expression


def regular_expression_extract(extract_data, request_result):
    for extract_key, extract_value in extract_data.items():
        extracted_value = re.search(extract_value, request_result)
        if extracted_value:
            search_value = extracted_value.group(1)
            YamlUtil().write_extract_yaml({extract_key: search_value})
        else:
            pytest.warns(allure_regular_expression(extracted_value, extract_key, extract_value, request_result))
