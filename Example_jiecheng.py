#-*- coding:utf-8 -*-

"""
10*9*8*7*6*5*4*3
"""
def jiecheng(n):
    if n<=1:
        return 1
    else:
        return n*jiecheng(n-1)

if __name__=="__main__":
    print jiecheng(10)