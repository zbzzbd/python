#-*-coding:utf-8 -*-

"""
某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，
加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换
"""

def encryption(parmater):
    par=[]
    if isinstance(parmater,int) and parmater/1000>=1:
        par.append(parmater/1000)
        par.append(parmater/100%10)
        par.append(parmater/10%10)
        par.append(parmater%10)
    else:
        raise KeyboardInterrupt("数据or 类型不正确")

    for i in range(0,4):
        par[i]=(par[i]+5)%10

    for i in range(0,2):
        n=-(i+1)
        par[i],par[n]=par[n],par[i]

    print par



if __name__=='__main__':
    parmater=int(raw_input('please input a num of four'))
    encryption(parmater)




