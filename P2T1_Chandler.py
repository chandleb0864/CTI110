#This program inputs student name, gpa, age, total sales, and sales tax percentage.
#It prints student name, gpa, total sales, profit, and sales tax.
#CTI 110
#M2T1
#B Wayne Chandler Jr
#11/01/2018
StudentName="Wayne"
StudentGPA=3.2
StudentAge=25
print("Hello",StudentName,"your GPA is",StudentGPA,"but you are not",StudentAge,"years old!")
#print("Hello",StudentName)
total_sales = float(input('Enter the projected sales: '))
print("Total sales = $",format(total_sales,",.2f"),sep='')
profit=total_sales*0.23
print("The profit is $",format(profit,",.2f"),sep='')
salesTax_percent=float(input("Enter sales tax percentage: "))
SalesTax=total_sales*((salesTax_percent)/100)
print("Sales Tax is $",format(SalesTax,",.2f"),sep='')




