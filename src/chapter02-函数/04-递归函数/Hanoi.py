#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#利用递归函数移动汉诺塔

def move(n,a,b,c):
    if n == 1:
        print('move',a,'--->',c)  #直接把盘子从a移到c
    else: #如果a有n个盘子(n > 1)，那么分三步
        move(n-1,a,c,b) #先把上面n-1个盘子，借助c，从a移到b
        move(1,a,b,c) #再把最下面的1个盘子，借助b，从a移到c
        move(n-1,b,a,c) #最后把n-1个盘子，借助a，从b移到c

move(3,'A','B','C')
