employee_name = str(input("Enter employee's name: "))
hours_worked_in_a_week = eval(input("Enter number of hours worked in a week: "))
hourly_pay_rate = float(input("Enter hourly pay rate: "))
month = str(input('Enter the month: '))
federal_tax = float(input("Enter federal tax withholding rate: "))
state_tax = float(input("Enter state tax withholding rate: \n"))

gross_pay = hourly_pay_rate * hours_worked_in_a_week
federal_withholding = federal_tax * 0.01 * gross_pay
state_withholding = state_tax * 0.01 * gross_pay

total_deduction = federal_withholding + state_withholding

net_pay = gross_pay - total_deduction

print('Divine Mercy Payroll statement for the month of ', month)
print('Employee Name:', employee_name)
print(f'Hours Worked: {hours_worked_in_a_week:.1f}')
print(f'Pay Rate:${hourly_pay_rate:.2f}');
print(f'Gross Pay:${gross_pay:.1f}')
print('Deductions:')
print(f'Federal Withholdings({federal_tax}%):${federal_withholding:.1f}')
print(f'State Withholdings({state_tax}%):${state_withholding:.2f}')
print(f'Total Deduction:${total_deduction:.2f}')
print(f'Net Pay:${net_pay}')