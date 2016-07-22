#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Parent:
    parentAttr =100


    def __init__(self):
        print "调用父类构造函数"

    def getAttr(self):
        print "调用父类属性",Parent.parentAttr

class Child(Parent):

    def __init__(self):
        print "调用zi类构造方法"

    def chilidMethod(self):
        print "调用zi类方法"


c = Child()
c.chilidMethod()
c.getAttr()



