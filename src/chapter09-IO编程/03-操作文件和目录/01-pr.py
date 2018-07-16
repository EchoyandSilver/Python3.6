#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 利用os模块编写一个能实现dir -l输出的程序。

import os
def dir_l(path = '.'):
    if path == '.':
        L = os.listdir(os.path.abspath(path))
    else:
        L = os.listdir(path)
    for dir in L:
        dir = os.path.join(path,dir)
        if os.path.isdir(dir):
            print(dir)
path = input('请输入一个文件夹路径，如果不输入则默认当前目录：')

print(dir_l(path))
