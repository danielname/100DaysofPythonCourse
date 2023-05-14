from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)

lines = Turtle(visible=False)
lines.color("white")
lines.speed(0)
lines.penup()
lines.goto(0, -290)
lines.pendown()
lines.seth(90)
for _ in range(20):
    lines.fd(15)
    lines.penup()
    lines.fd(15)
    lines.pendown()



screen.exitonclick()