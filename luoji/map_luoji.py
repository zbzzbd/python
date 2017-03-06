#-*- coding:utf-8 -*-

"""
map / reduce 练习
"""

def usally_execute():
    """
    本函数主要实现 将一个list放入另外一个list中
    """
    l=[]
    for i in [1,2,3,4,5]:
        l.append(i)
    print l

def execute(x):
    return x*x


def map_execute(list1):
    l=[]
    for n in list1:
        l.append(execute(n))
    print l

def add(x,y):
    return x*y

def is_ood(n):
    """
    判断是否为奇数
    """
    return n %2 ==1


if __name__=='__main__':
    usally_execute()
    print map(execute,[1,4,6,7])#map()作为高阶函数，事实上它把运算规则抽象了
    map_execute([1,2,4,5])

    print reduce(add,[1,3,5])#reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
    print filter(is_ood,[1,2,3,4,5,6])#filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素