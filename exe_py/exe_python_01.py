#-*- coding:utf-8 -*-

"""
输入某年某月某日，判定是今年的某天

1.根据输入的年份来断定2月份是28天还是29天
2.根据输入的月份来断定加到几月份

"""
class CountDay(object):

    def __init__(self):
        self.mouthDay=[31,28,31,30,31,30,31,30,31,30,31,30]

    def Get_Februray_Day(self,year):
        if (int(year)/1000>=1):
            if (int(year) %4==0 and int(year)%100==0  or int(year)%400==0):
                self.mouthDay[1]=29
        else:
            raise Exception("输入的年份不合法")


    def Get_Day_Acroding_mouth(self,mouth,day):

        if(0<mouth<=12 and self.mouthDay[mouth-1]>=day):
            sum=0
            for i in range(0,mouth-1):
                sum =sum+self.mouthDay[i]
            return  sum+day
        elif(mouth<0 or mouth>12):
            raise Exception("请输入合法的月份")
        else:
            raise Exception("输入的月份与日期不符合要求")


    def Year_mouth_day(self,year,mouth,day):
        """
        用来接收数据，判断输入的YEAR,MOUTH,DAY是否合法
        """
        if (year%1000<0):
            print "输入的年份不合法"
        elif(mouth>12 or mouth<0):
            print "请输入合法的月份"
        elif(self.mouthDay[mouth-1]!=day):
            print "请输入合法的天数"


if __name__ =="__main__":

    year=int(raw_input('请输入年份'))
    mouth=int(raw_input('请输入月份'))
    day = int(raw_input('请输入日'))
    countDay= CountDay()
    countDay.Get_Februray_Day(year)
    dayCout =countDay.Get_Day_Acroding_mouth(mouth,day)
    print "今天是%d 年的第 %d 天" %(year,dayCout)



