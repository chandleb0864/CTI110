#this program will print  a table of celsius to fahrenheit temps
#from 0 to 20
#CTI 110
#P4HW2_CelsiusFahrenheit_BeltonChandler
#B Wayne Chandler Jr
#11/27/2018

#print what the program does
#print table headings and separator
#calculate and print temperatures

def main():

    #tell what program does
    print()
    print ("This program displays a table of Celsius temperatures")
    print ("0 through 20 and their Fahrenheit equivalents")       

    #print table headings and separator
    print()
    print ("Celsius\tFahrenheit")
    print ("-------------------")

    #calculate and print temperatures
    for celsius in range (0, 21):
        fahrenheit = (((9/5)* celsius) + 32)
        print (celsius, "\t", format(fahrenheit,".1f"))

main()
