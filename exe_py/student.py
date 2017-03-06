#-*- coding:utf-8 -*-

"""
@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性


有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量
"""

class Student(object):

    def __init__(self,name):
        self.name = name

    def __str__(self):
        return 'student object (name:%s)' % self.name

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integeter')
        if value<0 or value >100:
            raise ValueError('score must between 0-100')

        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,value):
        self._birth=value

    @property
    def age(self):
        return 2014 -self._birth

if __name__=='__main__':
    s = Student('test')
    print s
    s.score=100
    print s.score

