#-*-coding:utf-8 -*-

def genNum(n):
    i=1
    while i <=n:
        yield  i**2
        i+=1


def deco(genNum):
    def wrapper(x):
        print "say something"
        genNum(x)
        print "no zuo no die"
    return wrapper
@deco
def show(x):
    print "i am from mars"

if __name__=="__main__":
    show(10)
    #g1=genNum(20)
#        print i
