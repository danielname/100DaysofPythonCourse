from turtle import Turtle, Screen
from player import Player
from ball import Ball
from scoreboard import ScoreBoard

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
score = ScoreBoard()


screen.listen()
screen.onkey(p1.move_up, "w")
screen.onkey(p1.move_down, "s")
screen.onkey(p2.move_up, "Up")
screen.onkey(p2.move_down, "Down")

screen.tracer(1)
while True:
    ball.fd(10)
    # paddle collision
    if (-340 >= ball.xcor() >= -345 and ball.distance(p1) < 50) or (345 >= ball.xcor() >= 340 and ball.distance(p2) < 50):
        ball.paddle_bounce()
    # wall collision
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.wall_bounce()
    # left miss
    if ball.xcor() < -400:
        ball.reset_position()
        score.r_point()

    # right miss
    if ball.xcor() > 400:
        ball.reset_position()
        score.l_point()


screen.exitonclick()
