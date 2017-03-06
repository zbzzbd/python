# -*- coding:utf-8 -*-
"""
求0—7所能组成的奇数个数。
1.范围  0-7
2.判断奇数
3.求个数
"""

import os

print "当前文件具体路径为：%s"%os.path.abspath(__file__)
print "当前文件路径%s"%os.path.dirname(os.path.abspath(__file__))
print os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print ord('4')-ord('2')

n =0
p = raw_input('input a octal number:\n')
j = len(p)

for i in range(j):

    n = n*8+ord(p[i])- ord('0')
    print i,n
print n