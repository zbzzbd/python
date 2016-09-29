#*-*- coding:utf-8 -*-

"""
暂停1秒输出
"""
import time

myD={'1':'a','2':'b'}
print dict.items(myD)
print time.strftime('%m-%d',time.localtime(time.time()))

for key,value in dict.items(myD):
    print key,value
    time.sleep(1)
