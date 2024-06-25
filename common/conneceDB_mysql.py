# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:简单
# @Time ： 2024/6/25 17:34
# software: PyCharm



import pymysql

import pymysql

# 替换以下参数为你的数据库信息
host = '192.168.0.223'
user = 'devuser'
password = '123456Test'
database = 'pbb-dev'  # 确保这里指定了数据库名称

# 创建数据库连接
connection = pymysql.connect(host=host, user=user, password=password, db=database)

# 使用连接进行操作...
