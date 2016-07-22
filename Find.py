#-*-coding:UTF-8 -*-
"""
查找字符串
"""

def FindStr(str,str1):
    return str.find(str1)


if __name__=='__main__':
    str='hello'
    str1='he'
    print FindStr(str,str1)

