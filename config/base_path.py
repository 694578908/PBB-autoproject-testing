# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:简单
# @Time ： 2024/6/20 16:36
# software: PyCharm

import os


# 当前绝对路径
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = os.path.dirname(BASE_PATH)

# 数据源存储路径
case_data_dir = os.path.join(BASE_PATH, 'testdata')
# 临时报告存储路径
report_dir_temp = os.path.join(BASE_PATH, 'report_temp')
# 报告存储路径
report_dir = os.path.join(BASE_PATH, 'report')
# 存放用例位置
TEST_CASE_DIR = os.path.join(BASE_PATH, 'testcases')

# host相关

app_HOST_GATEWAY="http://139.9.34.76:8930"
web_HOST_GATEWA="http://139.9.34.76:8009/"