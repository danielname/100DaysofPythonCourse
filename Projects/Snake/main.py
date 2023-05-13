import time
from turtle import Screen
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()
game = True

while game:
    screen.update()
    time.sleep(.1)
    snake.move()
#     detect collision with food
    if snake.head.distance(food) < 12:
        food.refresh()



screen.exitonclick()