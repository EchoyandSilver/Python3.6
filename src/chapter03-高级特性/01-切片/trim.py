#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：

def trim(L):
    if L[:1] is ' ':
        return trim(L[1:])
    elif L[-1:] is ' ':
        return trim(L[:-1])
    else:
        return L

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
