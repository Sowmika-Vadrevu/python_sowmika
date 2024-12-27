#prgm to read the employee name,designation,salary,special allowances,bonus as input frm user
''' i) gross monthly salary(sal+special allowance)
    ii) gross annual salary(gross monthly salary*12+bonus)
    iii)claculate the taxable income( nnual salray-tax)
     if salary>500000------------15%tax
        salary>400000------------10%tax
        salary>100000------------02%tax 
'''
        
emp_name=input("Enter the Employee name: ")
designation=input("Enter the designation: ")
sal=int(input('Enter the Salary: '))
special_allowance=int(input('Enter special allowance: '))
bonus=int(input('Enter the Bonus: '))
gross_month=sal+special_allowance
gross_annual=(gross_month*12)+bonus
print('Employee Details: ')
print('------------------')
print('Employee name:',emp_name)
print('Designation:',designation)
print('Salary:',sal)
print('special allowance:',special_allowance)
print('bonus:',bonus)
print('gross monthly salary:',gross_month)
print('gross annual salary:',gross_annual)
if(gross_annual>500000):
    taxable=gross_annual-((gross_annual*15)/100)
    print("taxable income is:",taxable)
elif(gross_annual>400000):
    taxable=gross_annual-((gross_annual*10)/100)
    print("taxable income is:",taxable)
else:
    taxable=gross_annual-((gross_annual*2)/100)
    print("taxable income is:",taxable)
