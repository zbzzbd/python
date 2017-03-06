#-*-coding:utf-8 -*-
"""
利用递归的方式求 5！
分析：所谓的阶乘：就是自己调用自己
2.利用递归的方式，将输入的5个字符串，以相反的顺序打印出来
分析：1.把输入的5个字符串存储起来，比如放入一个LISTzhong
2.使用递归的方式反向取出来

"""

def jiecheng(n):
    ji=1
    if n==0:
        ji=1
    else:
        print n
        ji=n*jiecheng(n-1)

    return  ji


def get_str():
    list=[]
    for i in range(5):

        str=raw_input("please input someting")
        list.append(str)
    return  list,len(list)

def jiecheng_zifu_print(list,len):
    if len-1<0:
        return
    print list[len-1]
    jiecheng_zifu_print(list,len-1)




if __name__ =="__main__":
    print jiecheng(3)
    list,length=get_str()
    jiecheng_zifu_print(list,length)