import re

from common.read_write_yaml import YamlUtil


def regular_expression_extract(extract_value, request_result):
    for key, regex_pattern in extract_value.items():
        extracted_value = re.search(regex_pattern, request_result)
        if extracted_value:
            YamlUtil().write_extract_yaml({key: extracted_value.group(1)})
