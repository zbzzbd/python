#!/usr/bin/python
# -*- coding: UTF-8 -*-

def chengji(n):
    ji=1
    for i in range(1,5):
        ji=ji*i
    return ji


def fact(j):
    sum =0
    if j==0:
        sum=1
    else:
        sum = j * fact(j-1)
    return sum

def age(n):
    if n==1 :
        c=10
    else:
        c=age(n-1) +2
    return c

if __name__=='__main__':
   ji=chengji(3)
   print ji
   print age(5)

