# This program will keep a running total of bugs for seven days.
# CTI 110
# P4T2 - Bug Collector
# B Wayne Chandler Jr
# 11/20/2018

#Initialize a counter
#input number of bugs each day
#Keep a total of bugs
#display total bugs

def main():


    #initialize the accumulator    
    total = 0

    #how many bugs each day    
    for day in range (1,8):

        # ask for nuber of bugs
        print("How many bugs were caught on day", day)

        # input number of bugs
        bugs = int(input())

        # total up the bugs
        total += bugs

    #display the total amount of bugs
    print("You collected a total of", total, "bugs.")
    
        
                        
main()       

    
