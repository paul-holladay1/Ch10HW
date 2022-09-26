# 2) EmployeeClass.py - Write a class named Employee that holds the following data about an employee in attributes: name, ID number, 
# department, job title and monthly salary.The Employee class’s __init__ method should accept an argument for each attribute. 
# The Employee class should have accessor methods for each attribute. All attribute should be hidden.

class Employee:

    def __init__(self, name, ID, department, job, salary):
        self.__name = name
        self.__ID = ID
        self.__department = department
        self.__job = job
        self.__salary = salary
    
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name
    
    def setID(self, ID):
        self.__ID = ID

    def getID(self):
        return self.__ID
    
    def setDepartment(self, department):
        self.__department = department

    def getDepartment(self):
        return self.__department
    
    def setJob(self, job):
        self.__job = job

    def getJob(self):
        return self.__job
    
    def setSalary(self, salary):
        self.__salary = salary

    def getSalary(self):
        return self.__salary