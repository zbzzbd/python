#-*-coding:utf-8 -*-

#用户判断质数

def is_prime(n):
    if n <=1:
        return False
    for i in range(2,n):
        if n % i ==0:
            return False
    return True


if __name__=='__main__':
    print is_prime(13)