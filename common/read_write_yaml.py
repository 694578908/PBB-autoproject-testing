import os

import pytest
import yaml
import re


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

    # 读取yml文件
    def read_testcase_yaml(self, yaml_name=None, key_name=None):
        if yaml_name is None:
            yame_name_message = 'yaml_name文件名称不能为空'
            pytest.fail(yame_name_message)

        yaml_path = os.path.join(os.getcwd(), 'data', yaml_name)
        if not os.path.exists(yaml_path):
            yaml_path_message = f'当前路径下:{yaml_path}没有该文件:{yaml_name}'
            pytest.fail(yaml_path_message)
        with open(os.getcwd() + "/data/" + yaml_name, mode='r', encoding='utf-8')as f:
            value = yaml.safe_load(stream=f)
            if yaml_name:
                return value[key_name]
            else:
                key_name_message = f'当前文件:{yaml_name}里的key没有被定义'
                pytest.fail(key_name_message)

            return value

    # 清除extract.yml
    def clear_extract_yaml(self):
        with open(os.getcwd() + "/data/extract.yml", mode='w', encoding='utf-8')as f:
            f.truncate()
