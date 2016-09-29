#-*- coding:utf-8 -*-
import doctest
def sum(x,y):
    """
    >>> sum(1,2)
    3
    >>> sum(2,5)
    7
    """
    return x+y


if __name__=="__main__":
    """
     自己探测自己
    """
    doctest.testmod()