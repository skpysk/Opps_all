from re import X
from xml.dom import XML_NAMESPACE


class Employee:
    def __init__(self,xname,xsalary,xwork):
        self.name = xname
        self.salary = xsalary
        self.work = xwork
    def emp(self):
        return f"the name is {self.name} and salary is {self.salary} and work is {self.work}" #yha per self.name wala dena he nake xname
    def __add__(self,other):
        return self.salary + other.salary  # self ke bad pehle var or nechai var.salary
     # all operator will support here 
     # minus plus devide all documentation
     # mapping operator to function
     # <__main__.Employee object at 0x000001AE7D17F160> solution of this  # () youforgot this one bcz
    def __repr__(self):
         return self.emp()
    def __str__(self):
        return  self.emp()
x = Employee("sonu",350,"programmer")
y = Employee("aman",5,"manager")

#print(x+y) # ager add krna he like this you can use add special methdod
print(x)