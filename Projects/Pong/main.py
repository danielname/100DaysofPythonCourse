from turtle import Turtle, Screen
from player import Player

P2_START = (350, 0)
P1_START = (-350, 0)

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

p1 = Player()
p1.goto(P1_START)
p2 = Player()
p2.goto(P2_START)
screen.listen()
screen.onkey(p1.move_up, "w")
screen.onkey(p1.move_down, "s")
screen.onkey(p2.move_up, "Up")
screen.onkey(p2.move_down, "Down")


screen.exitonclick()