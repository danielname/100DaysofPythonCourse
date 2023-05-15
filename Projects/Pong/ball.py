from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.setheading(random.randint(0,359))
        self.color("white")
        self.penup()

