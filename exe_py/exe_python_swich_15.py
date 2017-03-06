# -*-coding:utf-8 -*-

if __name__ =='__main__':
    n=0
    p = raw_input('input a octal number:\n')
    t =p.find('.')
    print t
    if p.find('.')>0:
        print "请输入正整数"

    else:
        for i in range(len(p)):
            n = n*8+ord(p[i])-ord('0')
    print n
