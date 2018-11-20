# This program will used turtle graphics to draw a square and a triangle.
# CTI 110
# P4T1A_Chandler
# B Wayne Chandler Jr
# 11/20/2018


#Load turtle
#create a screen for turtle
#change turtle shape and color
#draw a square
#draw a triangle


import turtle               #loads turtle
win = turtle.Screen()       #makes screen for turtle
turtle.shape("turtle")      #change turtle shape and color
turtle.color("red")
turtle.penup()
turtle.forward(-150)        #change position
turtle.pendown()

for s in range(4):          #draw square
    turtle.forward(100)
    turtle.left(90)

turtle.penup()              #move turtle without drawing
turtle.forward(200)
turtle.pendown()

for t in range(3):          #draw triangle
    turtle.forward(100)
    turtle.left(120)

win.mainloop()              #wait for user to close window
