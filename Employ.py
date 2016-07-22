class Employee:
    empcount=0

    def __init__(self,name,salary):
        self.name=name
        self.salary= salary
        Employee.empcount +=1

    def dispalyCount(self):
        print ("total emplyee %d" %Employee.empcount)

    def displayEmployee(self):
        print "Name:",self.name


emp1 =Employee("zbz",2000)
print  emp1.displayEmployee()