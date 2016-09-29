#-*-coding: utf-8 -*-

import re
print(re.match('www','www.runoobo.com').span())#在起始位置开始匹配
print(re.match('com','www.runoob.com'))

print (re.match('www','www.runooo.com')).span()

line ="cats are smarter than dogs"
matchObj = re.match(r'(.*) are(.*?) .*',line,re.M|re.I)

if matchObj:
    print "matchObj.group():",matchObj.group()
    print "matchObj.group(1)",matchObj.group(1)
    print "matchObj.group(2)",matchObj.group(2)
else:
    print "No match"
"""
匹配的整个表达式的字符串，group() 可以一次输入多个组号，
在这种情况下它将返回一个包含那些组所对应值的元组。
"""

line2="Cats are smarter than dogs"
matchObj = re.match(r'dogs',line2,re.M|re.I)
if matchObj:
    print "match --> matchObj.group():",matchObj.group()
else:
    print "No match"

matchObj = re.search(r'dogs',line2,re.M|re.I)
if matchObj:
    print "search -->matchobj.group():",matchObj.group()
else:
    print "No match"


phone="2004-959-559"
num = re.sub(r'#.*$',"",phone)
print "phone Num:",num

num = re.sub(r'\D',"",phone)
print "Phone Num:",num
