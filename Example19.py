#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。
程序分析：关键是计算出每一项的值。
"""

Tn=0 #Tn代表每个项
Sn=[]
n = int(raw_input('n = "\n')) #n 代表个数
a = int(raw_input('a =:\n'))   #a 代表单个数字
for count in range(n):
    Tn=Tn+a
    a= a *10
    Sn.append(Tn)
    print Tn
"""
Apply function of two arguments cumulatively to the items of iterable,
from left to right, so as to reduce the iterable to a single value.
For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5).
"""
Sn= reduce(lambda x,y:x+y,Sn)
print Sn