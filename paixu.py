#-*- coding:utf-8  -*-

"""
如何实现倒序排序 ，FEDCBA
"""
a = 'ABCDEF'
b ='ABCDEF'
print a
#这是python一种独特的写法
print a[::-1]

def paxu(a,b):
    le=int(len(a))
    if le %2 ==0:
        for i in range(0,le):
            print int(le)-i
            b[int(le)-i]=a[i]




paxu(a,b)







