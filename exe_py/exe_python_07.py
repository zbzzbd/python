#-*-encoding:utf-8 -*-

"""
1.按逗号分隔列表,把列表变成以逗号分割的字符串,利用字符串的join 方法，进行串联

2.素数： 利用FOR 来确定范围，用一个数，再进行除以除了1和它本身以为的数也得用FOR循环来表明
"""
l= [1,2,3,4]
s1=','.join(str(n) for n in l)
print type(s1)

sum=0

for num in range(1,101):
    if num >1:
            for j in range(2,num):
                if (num%j)==0:
                    break
            else:
                sum += num
                print num


print sum

