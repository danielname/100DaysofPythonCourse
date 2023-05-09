from turtle import Turtle, Screen
from random import randint, choice

timmy = Turtle()
timmy.shape("turtle")

screen = Screen()
screen.colormode(255)
# timmy.forward(50)
# timmy.right(45)
# timmy.forward(25)
# timmy.left(90)
# timmy.back(75)
# timmy.left(90)
# timmy.forward(75)
# timmy.right(90)
# timmy.forward(25)
# timmy.right(45)
# timmy.forward(10)

# Exercise 18-1
# Draw a square
# for num in range(0,4):
#     timmy.forward(100)
#     timmy.right(90)


# Exercise 18-2
# draw a dashed line with 10 dashes
# for _ in range(15):
#     timmy.fd(10)
#     timmy.penup()
#     timmy.fd(10)
#     timmy.pendown()

# Exercise 18-3
# draw regular shapes from 3 to 10 sides
# for num in range(3, 11):
#     r = randint(0,255)
#     g = randint(0,255)
#     b = randint(0,255)
#     timmy.pencolor(r, g, b)
#     for _ in range(num):
#         timmy.forward(100)
#         timmy.right(360/num)


# Exercise 18-4
# Draw a random walk
# timmy.width(10)
# directions = [0, 90, 180, 270]
timmy.speed(0)
# for _ in range(200):
#     r = randint(0,255)
#     g = randint(0,255)
#     b = randint(0,255)
#     timmy.pencolor(r, g, b)
#     timmy.setheading(choice(directions))
#     timmy.forward(20)


# Exercise 18-5
for _ in range(100):
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    timmy.pencolor(r, g, b)
    timmy.circle(100)
    timmy.left(3.6)



screen.exitonclick()