#This program will convert an integer from 1 to 10 to its
#roman numeral equivalent.
# CTI-110 
# P3HW1 - Roman Numerals 
# B Wayne Chandler Jr 
# 11/13/2018
#

#Ask for a whole number from 1 to 10.
#Decide what number has been input and print the
#equivalent roman numeral.
#Give error message if number is not in the 1 to 10 range.

#Ask for the number from 1 to 10.
number = int(input("Enter a whole number from 1 to 10: "))

#Decides what number was entered and prints roman numeral.
if number == 1:
    print ("The Roman Numeral equivalent is: I")
elif number == 2:
    print ("The Roman Numeral equivalent is: II")
elif number == 3:
    print ("The Roman Numeral equivalent is: III")
elif number == 4:
    print ("The Roman Numeral equivalent is: VI")
elif number == 5:
    print ("The Roman Numeral equivalent is: V")
elif number == 6:
    print ("The Roman Numeral equivalent is: VI")
elif number == 7:
    print ("The Roman Numeral equivalent is: VII")
elif number == 8:
    print ("The Roman Numeral equivalent is: VIII")
elif number == 9:
    print ("The Roman Numeral equivalent is: IX")
elif number == 10:
    print ("The Roman Numeral equivalent is: X")
    
#Gives error message if number not from 1 to 10
else:
    print ("Error! Please enter a whole number from 1 to 10")
