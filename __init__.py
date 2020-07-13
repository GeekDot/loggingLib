#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import logging

from datetime import datetime


# loggingLib
class LoggingLib(object):

    def __init__(self, path=None):

        # 实例化 logging
        self.logger = logging.getLogger()

        # 日志文件目录
        dt = datetime.now().strftime('%Y-%m-%d')
        if path is not None:
            # 自定义日志文件目录
            self.log_dir = os.path.join(path, dt)
        else:
            # 默认日志文件目录（当前目录）
            self.log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), dt)

        # 日志级别
        self.level_list = {
            'debug': logging.DEBUG,
            'info': logging.INFO,
            'warning': logging.WARNING,
            'error': logging.ERROR,
            'critical': logging.CRITICAL,
        }

        # 日志格式
        self.log_format = logging.Formatter("%(asctime)s - [%(levelname)s]: %(module)s.%(funcName)s(line:%(lineno)d)"
                                            " ==> '%(pathname)s' - %(message)s", datefmt='%Y-%m-%d %X')

    # 文件输出流
    def _file_stream(self, log_file):

        # 判断当前日期日志目录是否为空，如果为空则新建
        if not os.path.exists(self.log_dir):
            os.mkdir(self.log_dir)

        # 日志绝对路径
        log_abs_path = os.path.join(self.log_dir, log_file)

        file_stream = logging.FileHandler(log_abs_path)

        # 文件输出流设置日志格式
        file_stream.setFormatter(self.log_format)

        # 将志格式添加到文件输出流
        self.logger.addHandler(file_stream)

    # 屏幕输出流
    def _screen_stream(self):

        screen_stream = logging.StreamHandler()

        # 屏幕输出流设置日志格式
        screen_stream.setFormatter(self.log_format)

        # 将志格式添加到屏幕输出流
        self.logger.addHandler(screen_stream)

    # 日志文件层级
    @staticmethod
    def _dir_layer(name, layer):

        dt = datetime.now().strftime('%Y-%m-%d_%H')

        name_list = [i for i in name.split(os.path.sep) if i != '']
        count = len(name_list)

        if 0 < layer <= count:
            file_name = '_'.join(name_list[-layer:]).split('.')[0] + '_' + dt + '.log'
            return file_name
        else:
            file_name = '_'.join(name_list).split('.')[0] + '_' + dt + '.log'
            return file_name

    # 获取 logger
    def get(self, name, level='info', layer=3):

        # 获取日志文件名
        log_file = self._dir_layer(name, layer)

        # 设置日志级别，默认 INFO
        log_level = self.level_list[level]
        self.logger.setLevel(log_level)

        # 文件输出流
        self._file_stream(log_file)

        # 屏幕输出流
        self._screen_stream()

        return self.logger


log = LoggingLib()
