from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def move_foreward():
    tim.forward(10)


screen.listen()
# onkey is a higher order function: a function that can work with other functions
screen.onkey(key="space", fun=move_foreward)

screen.exitonclick()