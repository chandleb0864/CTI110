#This program will use turtle to print my initials
#CTI 110
#B Wayne Chandler Jr
#11/20/2018

#load turtle graphics
#create screen
#change shape and color
#reposition turtle to center letters better
#draw initials

import turtle           #load turtle
win = turtle.Screen()   #change shape color and reposition
turtle.shape("turtle")
turtle.color("red")
turtle.pensize(3)
turtle.penup()
turtle.forward(-150)
turtle.pendown()


turtle.forward(100)     #draw letter B
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.forward(-100)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(200)
turtle.left(90)

turtle.penup()          #draw letter C
turtle.forward(200)
turtle.pendown()
turtle.forward(100)
turtle.left(90)
turtle.penup()
turtle.forward(200)
turtle.pendown()
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(100)

win.mainloop()          #wait for user to close window




