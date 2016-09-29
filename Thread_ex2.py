# -*- encoding:utf-8 -*-
import  threading
import  time

exitFlag=0

class MyThread(threading.Thread):

    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print "starting" + self.name
        print_time(self.name,self.counter,5)
        print "exiting "+self.name


def print_time(threadName,delay,counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print "%s:%s" %(threadName,time.ctime(time.time()))
        counter-=1

if __name__=="__main__":
    thread1 = MyThread(1,"thread-1",1)
    thread2 = MyThread(2,"thread-2",2)

    thread1.start()
    thread2.start()

    print "Exiting main thread"