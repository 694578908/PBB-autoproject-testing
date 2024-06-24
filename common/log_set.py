# log_config.py
from datetime import datetime, timedelta
import logging
import os
import time


def setup_logger(name=None):
    # 日志级别映射关系
    level_relations = {'debug': logging.DEBUG, 'info': logging.INFO, 'warning': logging.WARNING,
                       'error': logging.ERROR, 'critical': logging.CRITICAL}
    # 日志格式
    fmt = '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s'
    # 设置日志级别为info
    level = 'info'

    # 获取当前脚本所在目录的上一级目录路径
    dirname_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    # 如果'log'目录不存在，则创建
    log_path = os.path.join(dirname_path, 'log')
    if not os.path.exists(log_path):
        os.mkdir(log_path)

    # 根据当前日期生成日志文件名
    logname = os.path.join(log_path, '{}.log'.format(time.strftime('%Y-%m-%d')))

    # 创建日志对象
    logger = logging.getLogger(name)
    formater = logging.Formatter(fmt)
    logger.setLevel(level_relations.get(level))

    # 创建输出到控制台的处理器
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formater)
    logger.addHandler(stream_handler)

    # 创建输出到文件的处理器
    file_handler = logging.FileHandler(logname, mode='a', encoding='utf-8')
    file_handler.setFormatter(formater)
    logger.addHandler(file_handler)

    return logger


# 初始化默认日志记录器
log = setup_logger()


# 定义计算当前时间-文件创建时间是否大于超时时间
def clear_logs(expiration_hours):
    expiration_hours = int(expiration_hours)
    log_file = os.getcwd() + "/log"
    log_path = os.path.abspath(log_file)
    current_time = datetime.now()
    if os.path.exists(log_path):
        lis = os.listdir(log_path)
        for filename in lis:
            file_path = os.path.join(log_path, filename)
            if os.path.isfile(file_path):
                file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
                time_difference = current_time - file_mtime
                if time_difference > timedelta(hours=expiration_hours):
                    os.remove(file_path)
    else:
        pass
