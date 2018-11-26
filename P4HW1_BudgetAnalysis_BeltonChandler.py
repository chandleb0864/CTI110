#This program keeps track of a budget and lets the user know if
#he has stayed within the budget or gone over budget
#CTI 110
#P4HW1_BudgetAnalysis_BeltonChandler
#B Wayne Chandler Jr
#11/20/2018

#Input amount budgeted for the month
#Enter monthyly bills
#keep a total of bills
#stop the loop
#determine if user is over or under budget
#print results

def main():
    
    #input monthly budget amount
    budgetAmount = float(input("How much money is budgeted for the month? "))
    
    
    #initialize accumulator
    subtotal = 0

    #variable to control loop
    anotherBill = "y"

    #enter amount of first bill
    firstBill = float(input("How much is the first bill? "))
    anotherBill = input("Is there another bill? Enter y for yes ")
    while anotherBill == "y" or anotherBill == "Y":

        #enter amounts of additional bills and keep subtotal       
        nextBill = float(input("Enter the amount of the next bill. "))
        anotherBill = input("Is there another bill? Enter y for yes ")
        subtotal = subtotal + nextBill
        
        
    #total of all bills
    total = firstBill + subtotal

    #calculate over or under budget
    underBudget = budgetAmount - total
    overBudget = total - budgetAmount

    #decide to print over or under budget and amount
    print()
    if total <= budgetAmount:
        print ("You are under budget by $", format(underBudget,\
              ",.2f"), sep = "")
    else:
        print ("You are over budget by $", format(overBudget, \
              ",.2f"), sep = "")  
        
    
       
            
main()
