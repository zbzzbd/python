
#!/usr/bin/env python

print 'hello, world','zbz','learn','python'
name = raw_input('please input your name')
print 'hello',name  

a =10
if a >0:
	print a
else:
	print -a
# array
classmate = ['a','b','c']
print classmate

classmate.append('d')
print classmate
classmate.pop() #delete
print classmate
className =('e','f','g')
print className
t = ('h','i','j',['A','B'])# tuple
print t
t[3][0]='X'
print t

# if else 
age = 20
if age >=18:
	print 'your age is ',age
	print 'adult'
else:
	print 'your age id ',age
	print 'teenager'

age = 3
if age >=18:
	print 'adult'
elif age >=6:
	print 'teenager'
else:
	print 'kid'
#for 
for name in classmate:
	print name
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
	sum =sum +x
print sum
# range
sum =0 
for x in range(101):
	sum = sum +x
print sum

#while
sum = 0
n =99
while n >0:
	sum = sum +n
	n = n -2
print sum
