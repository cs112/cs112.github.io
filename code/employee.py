######################################################
# OOP Example:  Employee
######################################################

class Employee(object):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def printEmployee(self):
        print ("Name: ", self.name)
        print ("Salary: ", self.salary)

    def getNetSalary(self):
        return 0.75*self.salary

    def isRich(self):
        return (self.salary > 100000)
        
    def salaryInFuture(self, years):
        return self.salary * 1.03**years

    def fire(self):
        self.salary = 0

e = Employee("Frank Underwood", 500000)
e.printEmployee()
print(e.getNetSalary())
print("Is", e.name, "rich?", "Yes!" if e.isRich() else "No!")
print(e.name, "salary in 10 years:", e.salaryInFuture(10))
e.fire()
e.printEmployee()
