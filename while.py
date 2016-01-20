#!/usr/bin/python
# -*- coding: utf-8 -*-
count = 0

while (count < 9) :
	print 'The count is :',count
	count = count + 1

print "Good bye!"

for letter in 'python':
	print '当前字母：',letter

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
	print '当前字母：',fruit

print "good bye!!"

for index in range(len(fruits)):
	print '当前水果：', fruits[index]

i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print i, " 是素数"
   i = i + 1

print "Good bye!"