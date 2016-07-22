#-*- coding: UTF-8 -*-
TRUE = 1
FALSE =0

def SQ(x):
    return x * x
print '如果输入的数字平方小于50，程序将停止'
again = 1
while again:
    num = int(raw_input('please input number'))
    print '运算结果为 %d' %(SQ(num))
    SQNum= SQ(num)
    if SQNum >=50:
        again =TRUE
    else:
        again = FALSE