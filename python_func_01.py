#-*- coding:utf-8 -*-
l1=[12,30,40,50]
m1=[1,2,3,4,5]
m2=['sun','m','T','F','s']
def f1(x):
    if x >20:
        return True
    else:
        return False

def f2_map(l1,l2):
    """
    其返回：[30, 40, 50]
    """
    print map(None,l1,l2)
def f3(x):
    return x*2

def f4(x,y):
    return x*2,y*2

def f2_map_1(l1):
    print map(f3,l1)

def f2_map_2(l1,l2):
    print map(f4,l1,l2)

def f5(x,y):
    return  x+y

def f5_reduce():
    print reduce(f5,l1)

def f5_reduce2():
    print reduce(f5,l1,10)
if __name__ =="__main__":
    print filter(f1,l1)
    f2_map(m1,m2)
    f2_map_1(l1)
    f2_map_2(m1,m2)
    f5_reduce()
    f5_reduce2()
