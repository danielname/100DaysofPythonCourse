from turtle import Turtle
from random import randint, choice


class Ball(Turtle):

    def __init__(self):
        super().__init__("circle")
        possible_directions = [randint(0,60), randint(120,179), randint(180,240), randint(300,359)]
        self.setheading(choice(possible_directions))
        self.color("white")
        self.penup()
        self.speed(1)

    def wall_bounce(self):
        self.setheading(360 - self.heading())

    def paddle_bounce(self):
        if self.heading() <= 180:
            self.setheading(180 - self.heading())
        else:
            self.setheading(540 - self.heading())
