# -*- encoding:utf-8 -*-
"""
两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。
a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单


分析：1.两队用2组数来表示，来进行比较 （1）ord,char,转化他们之间的关系

1.先表示拉开这两个队的数据
2.根据条件来确定名单

"""
list ={"x":None,"y":None,"z":None}
list1= list.keys()
list2=["c","b","a"]
print list1

"""
for i in range(ord('a'),ord('c')+1):
    for j in list1:
        if chr(i)=='c' and j!='x' and j!='z':
            list[j]=chr(i)

            list1.remove(j)
            print "aaaaa"
        elif chr(i)=='a' and j!='x':
            print "bbbbbb"
            list[j]=chr(i)
            list1.remove(j)
        elif chr(i)=='b':
            print "cccc"
            list[j]=chr(i)
"""

for i in list2:
    if i == 'c':
        for j in list1:
            if  j !='z' and j !='x':
                list[j]=i
                list2.remove(i)
                list1.remove(j)
    elif i =='a':
        for j in list1:
            if j != 'x':
                list[j] = i
                list1.remove(j)
                list2.remove(i)
    elif i == 'b':
        for j in list1:
            list[j] = i

print list
