import os
import  os.path
import pickle
#os.mkdir('d:/testDir')
#print os.getcwd()

#f1=open("robotframework.log","r+")
#print f1.readlines()
#print f1.tell()
#f1.seek(0,2)
#print f1.tell()
#f1.write("new line")
#f1.close()


#while True:
 #   g1=f1.next()
 #   print g1

filename="robotframework.log"

"""if os.path.isfile(filename):
    f1=open(filename,"a+")

while True:
    line = raw_input('input somting')
    if line =='q' or line =='quit':
        break
    f1.write(line+"\n")

d1={'y':567,'x':123}
pickle.dump(d1,f1)
f1.flush()"""

f2= open(filename,"r")
d2=pickle.load(f2)
print d2

f2.close()