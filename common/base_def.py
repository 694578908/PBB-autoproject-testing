# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:简单
# @Time ： 2024/6/25 19:21
# software: PyCharm



import json


class JsonData:

    #单一数据返回值，条件
    result_single_conditin = None
    # 列表数据返回值，无条件
    result_list = []
    # 多个数据返回值，条件
    result_list_conditin = []

    def get_singele_value_by_contition(self, json_data, key, value, source):
        '''

        :param json_data: 需要查询数据的json数据
        :param key: 判定的key
        :param value: 判定的value，于key是一对
        :param source: 返回的数据值的key名称
        :return:
        '''
        if self.return_value == None:
            if isinstance(json_data, dict):
                for item in json_data:
                    temp=json_data.get(key)
                    if item == key and json_data.get(key) == value:
                        self.result_single_conditin = json_data.get(source)
                    self.get_singele_value_by_contition(json_data.get(item), key, value, source)
            elif isinstance(json_data, list):
                for item in json_data:
                    self.get_singele_value_by_contition(item, key, value, source)
            else:
                pass

    def get_list_value_by_contition(self, json_data, key, value, source):
        '''

        :param json_data: 需要查询数据的json数据
        :param key: 判定的key
        :param value: 判定的value，于key是一对
        :param source: 返回的数据值的key名称
        :return:
        '''
        if isinstance(json_data, dict):
            for item in json_data:
                if item == key and json_data.get(key) == value:
                    self.result_list_conditin.append(json_data.get(source))
                self.get_list_value_by_contition(json_data.get(item), key, value, source)
        elif isinstance(json_data, list):
            for item in json_data:
                self.get_list_value_by_contition(item, key, value, source)
        else:
            pass

    def get_list_value(self, json_data, source):
        '''

        :param json_data: 需要查询数据的json数据
        :param key: 判定的key
        :param value: 判定的value，于key是一对
        :param source: 返回的数据值的key名称
        :return:
        '''
        if isinstance(json_data, dict):
            for item in json_data:
                if item == source:
                    self.result_list.append(json_data.get(source))

                self.get_list_value(json_data.get(item), source)
        elif isinstance(json_data, list):
            for item in json_data:
                self.get_list_value(item, source)
        else:
            pass



def merge(dict1:dict,dict2:dict):
    res={**dict1,**dict2}
    print(res)


if __name__=="__main__":
    dict1= {}
    dict2={}
    merge(dict1,dict2)