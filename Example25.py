#-*-coding:utf-8 -*-

a = int(raw_input("请输入一个数字:\n"))

x= str(a)
flage= True

for i in range(len(x)/2):
    if x[i] !=x[-i-1]:
        flage =False
        print x[-i -1]
        break

if flage:
    print "%d 是一个回文数！" %a
else:
    print "%d 不是一个回文数：" %a
