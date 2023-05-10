from random import choice
import colorgram as c
from turtle import Turtle, Screen

colors = c.extract('hirst.jpg',15)
color_list = []
for color in range(len(colors)):
    r=colors[color].rgb.r
    g=colors[color].rgb.g
    b=colors[color].rgb.b
    rgb = (r, g, b)
    color_list.append(rgb)

# Make a 10 x 10 painting
# each dot has a radius of 20
# gap between is 50
hirst = Turtle()
hirst.speed("fastest")
screen = Screen()
screen.colormode(255)
hirst.setheading(225)
hirst.penup()
hirst.fd(500)
hirst.pendown()
hirst.setheading(0)
for n in range(10):
    for m in range(10):
        hirst.color(choice(color_list))
        hirst.dot(20)
        if not m == 9:
            hirst.penup()
            hirst.forward(70)
            hirst.pendown()
    hirst.setheading(90)
    hirst.penup()
    hirst.forward(70)
    hirst.pendown()
    if n % 2 == 0:
        hirst.setheading(180)
    else:
        hirst.setheading(0)





screen.exitonclick()