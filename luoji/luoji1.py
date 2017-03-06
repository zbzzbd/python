#-*- coding:utf-8 -*-
"""
一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？

分析：1.开平方 math.sqrt  2.
"""
import math

for i in range(10000):

    x = math.sqrt(i+100)
    y = math.sqrt(i+268)

    if (x*x ==i+100)  and (y *y==i+268):
        print i






