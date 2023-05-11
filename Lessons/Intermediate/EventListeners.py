from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def move_foreward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    tim.left(15)

def turn_right():
    tim.right(15)

def clear_screen():
    tim.clear()

screen.listen()
# onkey is a higher order function: a function that can work with other functions
# screen.onkey(key="space", fun=move_foreward)


# Exercise 19-1
# make etch-a-sketch
screen.onkey(key="w", fun=move_foreward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()