# This program takes a number grade and converts to a letter grade.
# CTI 110
# P3LAB_Chandler
# B Wayne Chandler Jr
# 11/13/2018


#Input the numerical grade.
#Decide what the numerical grades equivalent letter grade is.
#Print the letter grade.


def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    
    # Input the numerical grade
    score = float(input('Enter grade: '))

    # Decide what the letter grade is and print the letter grade.
    if score >= A_score:
        print('Your grade is: A')
    else:
        if score >= B_score:
             print('Your grade is: B')
        else:
            if score >= C_score:
                print('Your grade is: C')
            else:
                if score >= D_score:
                    print('Your grade is: D')
                else:
                    print('Your grade is: F')




# program start
main()
