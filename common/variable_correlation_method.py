from common.read_write_yaml import YamlUtil


# 接口关联方法
def readextract_and_replacevariables(case):
    extract_value = YamlUtil().read_extract_yaml('extract.yml')
    if extract_value is None:
        return case
    for case_key, case_vlaue in case.items():
        if case_vlaue is None:
            continue
        request = case_vlaue
        # 遍历URL里的value是否有${{{}}}并且替换
        if 'url' in request and isinstance(request['url'], str):
            for key, value in extract_value.items():
                if f"${{{key}}}" in request['url']:
                    request['url'] = request['url'].replace(f"${{{key}}}", str(value))

        # 遍历headers里的value是否有${{{}}}并且替换
        if 'headers' in request and isinstance(request['headers'], dict):
            for key, value in request['headers'].items():
                if isinstance(value, str):
                    for new_key, new_value in extract_value.items():
                        if f"${{{new_key}}}" in value:
                            request['headers'][key] = value.replace(f"${{{new_key}}}", str(new_value))

        # 遍历headers里的value是否有${{{}}}并且替换
        if 'data' in request and isinstance(request['data'], dict):
            for key, value in request['data'].items():
                if isinstance(value, str):
                    for new_key, new_value in extract_value.items():
                        if f"${{{new_key}}}" in value:
                            request['data'][key] = value.replace(f"${{{new_key}}}", str(new_value))
                # 判断嵌套字典
                if isinstance(value, dict):
                    for new_key, new_value in extract_value.items():
                        for value_key, value_value in value.items():
                            if f"${{{new_key}}}" in str(value_value):
                                request['data'][key][value_key] = str(value_value).replace(f"${{{new_key}}}", str(new_value))
    return case
