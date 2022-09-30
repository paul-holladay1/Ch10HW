# 4) NetPay.py - write a program that will create the following employees (Table 1) as well as the payroll 
# deductions (Table 2):

import EmployeeClass as i

import PayrollDeductionClass as p

employee = i.Employee('Jimmy Smith', 58475, 'Information Systems', 'Developer', 6800)


charge1 = p.PayrollDeduction('food court', '8/14/2022', 22.50, 39119)
charge2 = p.PayrollDeduction('gift contribution', '8/12/2022', 25.00, 58475)
charge3 = p.PayrollDeduction('food court', '8/17/2022', 15.25, 21547)
charge4 = p.PayrollDeduction('vending machine', '8/22/2022', 3.00, 58475)
charge5 = p.PayrollDeduction('vending machine', '8/5/2022', 2.75, 58475)

charges = [charge1, charge2, charge3, charge4, charge5]

print('*** Employee Pay ***')
print('Name: ', employee.getName())
print('ID Number', employee.getID())
print('Department: ', employee.getDepartment())
print('Gross Pay: $', employee.getSalary(), sep='')

balance = employee.getSalary()

for charge in charges:
<<<<<<< HEAD
    if charge.getEmployeeID() == employee.getID():
        balance -= charge.getCharge()
print('Net Pay: $', balance, sep='')
=======
    if charge1.getEmployeeID() == employee.getID():
        balance =- charge.getCharge()
    # elif charge.getEmployeeID() == employee.getID():
    #     balance =- charge2.getCharge()  
    else:
        print('Net Pay: $', balance)
>>>>>>> 116b629c4c64fbfa0c6e8bcfcdb74abeff11a16b
