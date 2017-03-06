#-*- coding:utf-8 -*-

import  thread
import time
"""
线程调用thread模块中的start_new_thread()函数来产生新线程
"""

def print_time(threadName,delay):
    count = 0
    while count<5:
        time.sleep(delay)
        count+=1
        print "%s:%s" %(threadName,time.ctime(time.time()))

    # 创建两个线程

if __name__=="__main__":
    try:
        thread.start_new(print_time,("thread-1", 2, ))
        thread.start_new(print_time,("thread-2", 4, ))
    except:
        print "Error:unable to start thread"

    while 1:
        pass



