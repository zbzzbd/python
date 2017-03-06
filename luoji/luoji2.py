#-*- coding:utf-8 -*-

"""
输入某年某月某日，判断这一天是这一年的第几天？
影响天的因数：
1.平年与闰年的判断2月的天数
2.计算时，把n-1月的全部加上

"""

default_daylist=[31,28,31,30,31,30,31,31,30,31,30,31]  #

#根据年份获取
def get_februaryDay_according_year(year):

    if year%4==0 and year%100!=0 or  year %400 ==0:
        print '此年为闰年'
        default_daylist[1]=29
    else:
        print '此为平年'

    return default_daylist

#计算 天数

def count_day(mouth,day):
    days=0
    if 0<mouth<=1:
        days=day
        return days
    else:
        for i in range(mouth):
            print str(i+1) +"月"
            if i+1<mouth:
                month_day=default_daylist[i]
                days=days+month_day
            if i+1==mouth:
                days=days+day
    return  days

if __name__ =='__main__':
    year = int(raw_input('input year'))
    month = int(raw_input('input month'))
    day = int(raw_input('input day'))
    default_daylist=get_februaryDay_according_year(year)
    print count_day(month,day)

