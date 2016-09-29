#-*- encoding:utf-8 -*-
"""
   *
  ***
 *****
*******
 *****
  ***
   *

1.1个FOR 循环来控制打印空格，一个来控制打印*
关键是两个FOR 循环中如何打印出空格，打印多少*
"""
from sys import  stdout
for i in range(4):
    for j in range(2-i+1):
        stdout.write(' ')
    for k in range(2*i +1):
        stdout.write('*')
    print

for i in range(3):
    for j in range(i+1):
        stdout.write(' ')
    for k in range(4-2*i+1):
        stdout.write('*')
    print

