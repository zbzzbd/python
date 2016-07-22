#!/usr/bin/python
#-*-coding:UTF-8 -*-

if __name__ == '__main__':
    ptr = []
    for i in range(5):
        num = int(raw_input('pelase input a number:\n'))
        ptr.append(num)

    print ptr
    for i in ptr:
        print ptr[-i]