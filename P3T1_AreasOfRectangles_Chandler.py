#This program will determine the area of two rectangles and and give the
#rectangle with the greatest area or if rectangles have equal area.
#CTI 110
#P3T1_AreasOfRectangles_Chandler
#B Wayne Chandler Jr
#11/06/2018
#
#
#ask for length and width of first rectangle
#ask for length and width of second rectangle
#calculate area of first rectangle
#calculate area of second rectangle
#determine which rectangle as the greater area or if they have equal area
#print if a rectangle has greater area or if they are equal
#
#
#input area of rectangles
lengthFirst = float(input('What is the length of the first rectangle? '))
widthFirst = float(input('What is the width of the first rectangle? '))
lengthSecond = float(input('What is the length of the second rectangle? '))
widthSecond = float(input('What is the width of the second rectangle? '))


#calculate area of rectangles
areaFirst = (lengthFirst * widthFirst)
areaSecond = (lengthSecond * widthSecond)


#determine if rectangles are equal or if one is > than another
#and print results
if areaFirst > areaSecond:
    print ('The first rectangle has more area')
else:
    if areaSecond > areaFirst:
        print ('The second rectangle has more area')
    else:
        print ('Both rectangles have the same area')
           
