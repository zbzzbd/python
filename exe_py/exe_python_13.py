# -*- coding:utf-8 -*-
"""
读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。
1.如何获取7个数
2.判断改数的范围1-50
3.读取后并打印出该值的个数的*
"""

n=1
"""
while n <7:
    string=raw_input('please input a number')
    if string.isdigit():
        a = int(string)
        if a>=1 and a<=50:
            print '*'*a
        else:
            print "输入数字不在输入范围内"
            break
        n+=1
    else:
        print "请输入合法数字"
"""

deleimter ='-'
mylist ='abcd'
print deleimter.join(mylist)