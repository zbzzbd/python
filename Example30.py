#-*-coding:UTF-8 -*-
if __name__ =='__main__':
    a =[9,4,3,2]
    N = len(a)
    print a

    # for i in range (N):
    #     print a[-i-1]
    for i in range(N /2):
        a[i],a[N-i-1] = a[N-i-1],a[i]
    print a

# """
# 使用auto定义变量的用法。
# """
    num =1
    def autofunc():
        num =1
        print 'interanl block num=%d' %num
        num+= 1
    for i in range(3):
        print 'The num = %d' %num
        num +=1
        autofunc()