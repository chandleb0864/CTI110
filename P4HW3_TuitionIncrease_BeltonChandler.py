#This program will display a table of tuition increases over 5 years
#CTI 110
#P4HW3_TuitionIncrease_BeltonChandler
#B Wayne Chandler Jr
#11/27/2018

#Input the starting/current tuition amount per semester
#Determine/calculate increase of yearly tuition over 5 years
#Determine/calculate increase of tuition per semester over 5 years
#Print tuition increase for 5 years and projected semester increase



def main():

    #input starting semester tuition       
    startTuition = float(input\
                         ("How much is the starting tuition per semester? "))
    
    yearTuition = startTuition * 2  #calculate yearly tuition
    
    #print headers and separator
    print()
    print("Projected Semester Tuition Amount")
    print("of 3% Over the next 5 years")
    print()
    print("Year\tSemester\tTuition")
    print("-------------------------------")

            #calculate and print yearly tuition increase
    for year in range (1, 6):
        yearTuition = (yearTuition) * 1.03
        print (year, "\t\t\t$", format(yearTuition, ",.2f"), sep="")
        print()#blank row
    
            #calculate and print fall and spring tuition increase
        for semester1 in ["Fall"]:
            semesterTuition = (yearTuition / 2)
            print("\t",semester1, "\t\t$", format(semesterTuition, \
                                                  ",.2f"),sep = "")

            for semester2 in ["Spring"]:
                print("\t",semester2, "\t\t$", format(semesterTuition, \
                                                      ",.2f"),sep = "")
                print()#blank row
    
main() 
