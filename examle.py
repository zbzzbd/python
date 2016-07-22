#-*-coding: UTF-8 -*-
import time
#斐波那契数列

def fib(n):
    a,b =0,1
    for i in range(n-1):
        print a
        a,b=b,a+b
    return a

print fib(10)


#采用递归方法

def fib1(n):
    if n==1 or n==2:
        return 1
    return fib1(n-1)+fib1(n-2)
print fib1(10)


def fib3(n):
    if n==1:
        return [1]
    if n==2:
        return [1,1]
    fibs =[1,1]
    for i in range(2,n):
        fibs.append(fibs[-1]+fibs[-2])
    return fibs
print fib3(10)

#复制 使用[:]
a =[1,2,3]
b = a[:]
print b

#暂停一秒输出
myD ={1:'a',2:'b'}

for key,value in dict.items(myD):
    print key,value
    time.sleep(1) # 暂停