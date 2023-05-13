import time
from turtle import Turtle

class Snake:

    def __init__(self):
        self.segments = []
        for index in range(3):
            turtle = Turtle("square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(x=(0 - (index * 20)), y=0)
            self.segments.append(turtle)

    def move(self):
        for segment in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(x=new_x, y=new_y)
        self.segments[0].forward(20)