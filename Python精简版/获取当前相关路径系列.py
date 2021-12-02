#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os, sys


# 目录名
print('path ==>', sys.path[0])
# 文件名
print('file ==>', __file__)
# 文件名
print('argv ==>', sys.argv[0])
# 当前目录
print('getcwd ==>', os.getcwd())
# 真实路径
print('realpath ==>', os.path.realpath(__file__))
# 绝对路径
print('abspath ==>', os.path.abspath(__file__))
# 目录名
print('dirname ==>', os.path.dirname(os.path.abspath(__file__)))
# 分隔符
print('path.sep ==>', os.path.sep)
# 字符串连接
print(os.path.join(sys.path[0], __file__))
