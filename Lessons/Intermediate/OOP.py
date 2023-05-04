# #basic way to import a class
# import turtle
# # name = module.Class()
# new_turtle = turtle.Turtle()

# shorter
from turtle import Turtle, Screen
new_turtle = Turtle()
new_turtle.shape('turtle')
new_turtle.color('chartreuse4')
new_turtle.forward(100.00)

my_screen = Screen()
print(my_screen.canvheight)

my_screen.exitonclick()