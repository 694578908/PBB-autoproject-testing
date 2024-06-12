import os
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

        with open(os.getcwd() + "/data/extract.yml", mode='w', encoding='utf-8')as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)

