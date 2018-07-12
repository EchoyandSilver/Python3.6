#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#以下函数允许计算一个或多个数的乘积：

def product(x,*args):
    for i in args:
        x *= i
    return x
print(product(1,2,3,4,))
