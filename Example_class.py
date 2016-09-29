#-*-coding:utf-8 -*-
class FirstDemo():

    data = 'hello world'

    def __init__(self,who):
        self.data = who
    """
    析构函数，消除的作用，一般无需重载
    """
    def __del__(self):
        pass


    def printData(self):
        print self.data
    def setData(self,r):
        self.data=r

    def Read_file(self,path):
        try:
            fh = open(path,'r')
        finally:
            fh.close()

if __name__=='__main__':
    print FirstDemo(10).data
    print FirstDemo.__dict__
    print dir(FirstDemo)
    print dir(FirstDemo(10))
    FirstDemo(10).Read_file('/tmp/fiel.txt')
