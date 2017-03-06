#-*-coding:utf-8 -*-
from math import sqrt
"""
求100之内的素数
"""

def suNum():
    N = 100
    a = range(0, N) #0---100之间的list
    for i in range (2,int(sqrt(N))):
        for j in range(i+1,N):
            if (a[i] !=0) and (a[j] !=0):
                if a[j]%a[i]==0:
                    a[j]=0
    print

    for i in range(2,N):
        if a[i]!=0:
            print "%5d" %a[i]
            if (i -2) %10 ==0:
                print

def sortInsert():
    a = [1,4,6,8,9]
    print 'original list is :'
    for i in range(len(a)):
        print a[i]
    number = int(raw_input("insert a number:\n"))
    end = a[4]
    if number >end:
        a[4] =number
    else:
        for i in range(len(a)+1):
            if a[i]>number:
                tmp1= a[i]
                a[i]=number
                for j in range(i+1,len(a)+1):
                    tmp2 = a[j]
                    a[j] =tmp2
                    tmp1 =tmp2
                break
    for i in range(len(a)):
        print a[i]
if __name__=='__main__':
    #sortInsert()
    suNum()


