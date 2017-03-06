# -*- coding:utf-8 -*-
"""
按照逗号分割列表
"""

l= [1,2,3,4,5]
s1 = '*'.join(str(n)for n in l)
print s1

def get_shushu(start,end):

    for num in range(start,end+1):
        if num >1:
            for i in range(2,num):
                if num %i ==0:
                    break
            else:
                return num


if __name__ =="__main__":
    start=raw_input('输入左区间')
    end = raw_input()
    get_shushu()
