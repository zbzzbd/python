# -*- coding:UTF-8 -*-

import math
"""
有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？

"""

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i !=k)and (i !=j) and (j !=k):
                print i,j,k



i = int(raw_input('净利润：'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075]
r=0
for idx in range(0,5):
    if i>arr[idx]:
        r += (i - arr[idx]) * rat[idx]
        print (i-arr[idx])*rat[idx]
        i = arr[idx]
print r

for i in range(10000):
    x = int(math.sqrt(i+100))
    y = int(math.sqrt(i +268))
    if (x *x == i +100) and (y * y == i+268):
        print i