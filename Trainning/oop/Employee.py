__author__ = 'pratibh'

class Employee:
    count = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.count+=1

    def getCount(self):
        return Employee.count
emp1 = Employee("ram","1000")
emp2 = Employee("arun","100000")
emp3 = Employee("Hari","100")
print "Total Employee ", emp2.getCount()
