#This program will ask for a temperature in Celsius and
#then display it in Fahrenheit
#CTI 110
#B Wayne Chandler Jr
#11/01/2018
#ask for temperature in Celsius
celsiusTemp = float(input("Enter the temperature \
in degrees Celsius?: "))
#calculate fahrenheit temperature 9/5C+32
fahrenheitTemp = ((9/5)*(celsiusTemp) + 32)
#show the Fahrenheit temperature
print("The temperature in degrees Fahrenheit is",fahrenheitTemp)

