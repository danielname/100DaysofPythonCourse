import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

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
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score += 1
        score.update()
# game over on wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game = False
        score.game_over()
# game over on tail
    for segment in snake.segments:
        if segment != snake.head:
            if snake.head.distance(segment) < 10:
                game = False
                score.game_over()


screen.exitonclick()