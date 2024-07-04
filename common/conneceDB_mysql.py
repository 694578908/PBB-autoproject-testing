# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:简单
# @Time ： 2024/6/25 17:34
# software: PyCharm


import pymysql


# 创建数据库连接
def read_mysql(read_mysql_account):
    # 调取封装账号
    host, user, password, database = read_mysql_account
    connection = pymysql.connect(host=host, user=user, password=password, db=database)
