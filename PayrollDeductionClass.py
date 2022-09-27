# 3) PayrollDeductionClass.py - Write a class that represents a payroll deduction transaction. Each instance should have the 
# description, date, charge amount and employee ID as attributes. The class’s __init__ method should accept an argument for each 
# attribute. The class should have accessor methods for each attribute. All attribute should be hidden.

class PayrollDeduction:

    def __init__(self, description, date, charge, employeeID):
        self.__description = description
        self.__date = date
        self.__charge = charge
        self.__employeeID = employeeID

    def getDescription(self):
        return self.__description
    
    def getDate(self):
        return self.__date

    def getCharge(self):
        return self.__charge
    
    def getEmployeeID(self):
        return self.__employeeID