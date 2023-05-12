from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")

for index in range(3):
    turtle = Turtle("square")
    turtle.color("white")
    turtle.goto(x=(0 - (index * 20)), y=0)

screen.exitonclick()