#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 输出斐波那契数列的前N个数

# way 1
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

# way 2, generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

for n in fib(6):
    print(n)
