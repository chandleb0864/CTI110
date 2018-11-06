#This program will display the percentage of males and females in a class.
#CTI 110
#B Wayne Chandler Jr
#11/02/2018
#Input the number of males in the class
#Input the number of females in the class
#Calculate total number of students in class, males + females
#Calculate percentage of males, (males/total students)*100 ; same for females
#Display percentage of males and females in class.
#
#Inputs for males and females
numMales = int(input("How many males are in the class? "))
numFemales = int(input("How many females are in the class? "))
#Calculate toal students and percentages
totalStudents = numMales + numFemales
percentMale = (numMales/totalStudents)
percentFemale = (numFemales/totalStudents)
#Display formatted results
print ("The percentage of males in the class is ", format(percentMale,".0%"),\
       "\nand the percentage of females in the class is "\
       ,format(percentFemale,".0%"),sep='')
