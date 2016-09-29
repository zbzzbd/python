#-*- encoding:utf-8 -*-
"""

一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同

分析：回文数字特点：121,12321，
1.位数必须为奇数
2.第一个与最后一个相同，第二个与倒第二个相同

"""


def Panduan_Huiwen(x):
    flag = True
    if len(x)%2!=0:
        for i in range(len(x)/2):
            if x[i] !=x[-i-1]:
                flag =False
                break
        if flag:
            print "%s 是一个回文字符串" %x
        else:
            print "%s 不是一个回文字符串" %x
    else:
        print "%s 不是一个回文字符串" % x


if __name__ =="__main__":
    a = str(int(raw_input("请输入：\n")))
    Panduan_Huiwen(a)
