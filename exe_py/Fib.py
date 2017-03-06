#-*- coding:utf-8 -*-

"""
如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法
"""
class Fib(object):

    def __init__(self):
        self.a,self.b = 0,1

    def __iter__(self):
        return self

    def next(self):
        self.a ,self.b = self.b,self.a+self.b
        if self.a >1000:
            raise StopIteration()
        return self.a

if __name__ =='__main__':
    for n in Fib():
        print n