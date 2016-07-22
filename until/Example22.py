#/usr/bin/python
#-*-coding:utf-8 -*-

"""
程序分析：先把图形分成两部分来看待，前四行一个规律，后三行一个规律，利用双重for循环，第一层控制行，第二层控制列。
程序源代码：
"""
from sys import stdout
def printLst():
    for i in range(4):
        for j in range(7):
            stdout.write('*')
        print
def printLst2():
    for i in range(1):
        for j in range(2-i+1):
            stdout.write('1')
        for k in range(2*i +1):
            stdout.write('*')
        print

    # for i in range(3):
    #     for j in range(i+1):
    #         stdout.write(' ')
    #     for k in range(4-2*i +1):
    #         stdout.write('*')
    #     print
if __name__=='__main__':
    printLst2()
