#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#请使用迭代查找一个list中最小和最大值，并返回一个tuple：

def findMinAndMax(L):
    if L == []:
        return (None, None)
    else:
        for a in L:
            if a == max(L):
                break
        for b in L:
            if b == min(L):
                break
    return (b,a) 
L = [1,3,5,6]
print(findMinAndMax(L))

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
