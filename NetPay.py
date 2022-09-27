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

from tabulate import tabulate
table = [['Name', 'ID Number', 'Department', 'Job Title', 'Monthly Salary'], 
         [employee.getName(), employee.getID(), employee.getDepartment(), employee.getJob(), employee.getSalary()]]
print(tabulate(table))
print()

table = [['Description', 'Date', 'Charge', 'EmployeeID'],
         [p.PayrollDeduction.getDescription(charge1), p.PayrollDeduction.getDate(charge1), p.PayrollDeduction.getCharge(charge1), p.PayrollDeduction.getEmployeeID(charge1)],
         [p.PayrollDeduction.getDescription(charge2), p.PayrollDeduction.getDate(charge2), p.PayrollDeduction.getCharge(charge2), p.PayrollDeduction.getEmployeeID(charge2)],
         [p.PayrollDeduction.getDescription(charge3), p.PayrollDeduction.getDate(charge3), p.PayrollDeduction.getCharge(charge3), p.PayrollDeduction.getEmployeeID(charge3)],
         [p.PayrollDeduction.getDescription(charge4), p.PayrollDeduction.getDate(charge4), p.PayrollDeduction.getCharge(charge4), p.PayrollDeduction.getEmployeeID(charge4)],
         [p.PayrollDeduction.getDescription(charge5), p.PayrollDeduction.getDate(charge5), p.PayrollDeduction.getCharge(charge5), p.PayrollDeduction.getEmployeeID(charge5)]]
         
print(tabulate(table))
print()

print('*** Employee Pay ***')
print('Name: ', employee.getName())
print('ID Number', employee.getID())
print('Department: ', employee.getDepartment())
print('Gross Pay: $', employee.getSalary(), sep='')
print('Net Pay: $', employee.getSalary() - charge2.getCharge() - charge4.getCharge() - charge5.getCharge(), sep='')