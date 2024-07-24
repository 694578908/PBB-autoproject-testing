import os
import pytest
import yaml
from common.testcase_allure_reports import key_name_message, key_name_NoneMessage, yame_name_message, yaml_path_message, \
    YAMLError_exc_masssage


class YamlUtil:

    # 写入extract.yml
    def write_extract_yaml(self, data):
        data_dir = os.path.join(os.getcwd(), 'data')
        if not os.path.exists(data_dir):
            os.mkdir('data')
            yaml_path = os.path.join(data_dir, "extract.yml")
            if not os.path.exists(yaml_path):
                with open(yaml_path, mode='a', encoding='utf-8')as f:
                    pass

        with open(os.getcwd() + "/data/extract.yml", mode='a', encoding='utf-8')as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)

    # 创建文件夹
    def create_dir(self, dir_name):
        dir_path = os.path.join(os.getcwd(), dir_name)
        if not os.path.exists(dir_path):
            os.mkdir(dir_name)
        return dir_path

    # 读取extract.yml
    def read_extract_yaml(self, key):
        with open(os.getcwd() + '/data/' + key, mode='r', encoding='utf-8')as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value

    # 读取data的yml文件
    def read_testcase_yaml(self, yaml_name=None, key_name=None):
        if yaml_name is None:
            pytest.fail(yame_name_message(yaml_name))

        yaml_path = os.path.join(os.getcwd(), 'data', yaml_name)
        if not os.path.exists(yaml_path):
            pytest.fail(yaml_path_message(yaml_path, yaml_name))
        with open(os.getcwd() + "/data/" + yaml_name, mode='r', encoding='utf-8')as f:
            try:
                value = yaml.safe_load(stream=f)
                if key_name is not None:
                    if key_name in value:
                        return value[key_name]
                    else:
                        pytest.fail(key_name_message(key_name, value))
                else:
                    pytest.warns(key_name_NoneMessage())
                    return value
            except yaml.YAMLError as exc:
                YAMLError_exc_masssage(exc)

    def read_testcase_data_yaml(self, yaml_name=None, key_name=None):
        if yaml_name is None:
            pytest.fail(yame_name_message(yaml_name))

        yaml_path = os.path.join(os.getcwd(), 'testcases_data', yaml_name)
        if not os.path.exists(yaml_path):
            pytest.fail(yaml_path_message(yaml_path, yaml_name))
        with open(os.getcwd() + "/testcases_data/" + yaml_name, mode='r', encoding='utf-8')as f:
            try:
                value = yaml.safe_load(stream=f)
                if key_name is not None:
                    if key_name in value:
                        return value[key_name]
                    else:
                        pytest.fail(key_name_message(key_name, value))
                else:
                    pytest.warns(key_name_NoneMessage())
                    return value
            except yaml.YAMLError as exc:
                YAMLError_exc_masssage(exc)

    # 清除extract.yml
    def clear_extract_yaml(self, yaml_name):
        with open(os.getcwd() + "/data/" + yaml_name, mode='w', encoding='utf-8')as f:
            f.truncate()
