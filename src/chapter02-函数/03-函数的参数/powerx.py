#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#用来计算x的n次方
def power(x,n):
    s = 1
    while n > 0:
        n = n -1
        s = s*x
    return s
# example
print(power(5,2))
print(power(10,3))
