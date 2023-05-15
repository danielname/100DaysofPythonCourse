from turtle import Turtle, Screen
from player import Player
from ball import Ball

P2_START = (350, 0)
P1_START = (-350, 0)

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

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

p1 = Player(P1_START)
p2 = Player(P2_START)
ball = Ball()


screen.listen()
screen.onkey(p1.move_up, "w")
screen.onkey(p1.move_down, "s")
screen.onkey(p2.move_up, "Up")
screen.onkey(p2.move_down, "Down")

screen.tracer(1)
while True:
    ball.fd(10)
    if ball.distance(p1) < 15 or ball.distance(p2) < 15:
        ball.paddle_bounce()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.wall_bounce()

screen.exitonclick()
