#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#计算阶乘n! = 1 x 2 x 3 x ... x n，用函数fact(n)表示，可以看出：
#fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n
#利用递归计算阶乘

def fact(n):
    if n == 1:
        return 1
    return fact(n-1) * n
print(fact(5))

#计算过程：
#===> fact(5)
#===> 5 * fact(4)
#===> 5 * (4 * fact(3))
#===> 5 * (4 * (3 * fact(2)))
#===> 5 * (4 * (3 * (2 * fact(1))))
#===> 5 * (4 * (3 * (2 * 1)))
#===> 5 * (4 * (3 * 2))
#===> 5 * (4 * 6)
#===> 5 * 24
#===> 120
