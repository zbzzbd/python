#-*-coding:UTF-8 -*-

"""
输入三个整数，X,Y,Z ,请把这三个数从小到大输出
"""
l =[]

for i in range(3):
    x = int(raw_input('integer:\n'))
    l.append(x)

l.sort()
print l
