#!/usr/bin/python
# -*- coding: UTF-8 -*-
class JustCounter:
    __secretCount =0
    publicCount = 0

counter = JustCounter()
print counter.publicCount
print counter.__class__
print counter._JustCounter__secretCount  #访问私有变量