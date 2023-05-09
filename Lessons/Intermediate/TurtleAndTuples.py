from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
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
for _ in range(15):
    timmy.fd(10)
    timmy.penup()
    timmy.fd(10)
    timmy.pendown()


screen = Screen()
screen.exitonclick()