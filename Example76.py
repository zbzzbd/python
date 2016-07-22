# -*- coding:UTF-8 -*-

def peven(n):
    i =0
    s =0
    for i in range(2,n+1,2):
        s += 1.0/i
    return s

def podd(n):
    s = 0.0
    for i in range(1,n+1,2):
        s+= 1/i
    return s
def decall(fp,n):
    s = fp(n)
    return s

if __name__ =='__main__':
     n = int(raw_input('input a number:\n'))
     if n%2 ==0:
         sum = decall(peven,n)
     else:
         sum = decall(podd,n)
     print sum

     s = ["man","woman","girls","boy","sister"]
     for i in range(len(s)):
         print s[i]
