#-*- coding:utf-8 -*-
"""
在函数调用前后自动打印日志，但又不希望修改now()函数的定义,
这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
"""

def log(func):
    def wrapper(*args,**kw):
        print 'call %s()' %func.__name__
        return func(*args,**kw)
    return wrapper

def pr(text):
    def decator(func):
        def wrapper(*args,**kw):
            print 'call %s%s():'%(text,func.__name__)
            return func(*args,**kw)
        return wrapper
    return decator


@log
def now():
    print '.............'

@pr('hello world')
def priv():
    print '**************'


def log(func):
    def wrapper(*args,**kw):
        print 'call %s()' %func.__name__
        return func(*args,**kw)
    return wrapper

if __name__ == '__main__':
    f=now
    print f()
    print f.__name__

    h=priv
    print h()
