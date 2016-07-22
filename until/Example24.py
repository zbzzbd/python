#/usr/bin/python
#-*-coding:utf-8 -*-
"""
有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
"""

a= 2.0
b=1.0
s =0

for n in range(1,21):
    s += a/b
    t = a
    a =a +b
    b = t
print s



"""
求1+2!+3!+...+20!的和。
"""
sum=0
t=1
for n in range(1,21):
    t=t*n
    sum=sum+t

print t

"""
题目：利用递归方法求5!。
"""

def fact(j):
    sum=0
    if j ==0:
        sum=1
    else:
        sum= j*fact(j-1)
    return sum

for i in range(1,6):
    print '%d != %d' %(i,fact(i))


"""
利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来
"""
def output(s,l):
    if l==0:
        return
    print (s[l-1])
    output(s,l-1)
s = raw_input('input a staring:')
l = len(s)
output(s,l)
