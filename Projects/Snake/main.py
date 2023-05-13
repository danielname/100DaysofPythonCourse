import time
from turtle import Turtle, Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()

screen.update()
game = True

while game:
    screen.update()
    time.sleep(.1)
    snake.move()








screen.exitonclick()