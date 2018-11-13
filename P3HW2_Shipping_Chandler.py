#This program will calculate shipping charges for packages.
# CTI-110 
# P3HW2 - Shipping Charges 
# B Wayne Chandler Jr 
# 11/13/2018
#

#Enter the weight of the package.
#Determine shipping charge based on weight times rate.
#Print the shipping charge.

#Enter the weight of the package.
weight = float(input("What is the weight of the package? "))

#determine shipping rate based on weight
if weight <= 2:
    rate = 1.50
elif weight > 2 and weight <= 6:
    rate = 3.00
elif weight > 6 and weight <= 10:
    rate = 4.00
else:
    rate = 4.75

#calculate shipping rate
shipRate = weight * rate

#print shipping rate
print ("The shipping charges are $", format(shipRate, ",.2f"),\
       sep = "")
