#-*- coding:utf-8 -*-
"""
按相反的顺序输出列表的值。
"""
import  random
a =['one','two','three']

for i in a[::-1]:
    print i
tmp=0
for i in range(1,101):
    tmp +=i
print tmp

print random.uniform(10,20)