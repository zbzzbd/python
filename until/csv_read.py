import csv
date = csv.reader(open('info.csv','r'))

for user in date:
    print (user)