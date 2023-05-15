from turtle import Turtle
from random import randint, choice
possible_directions = [randint(0,60), randint(120,179), randint(180,240), randint(300,359)]


class Ball(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.current_speed = 1
        self.setheading(choice(possible_directions))
        self.color("white")
        self.penup()
        self.speed(self.current_speed)

    def wall_bounce(self):
        self.speed(0)
        self.setheading(360 - self.heading())
        self.speed(self.current_speed)

    def paddle_bounce(self):
        if self.heading() <= 180:
            self.speed(0)
            self.setheading(180 - self.heading())
            self.current_speed *= 1.2
            self.speed(self.current_speed)
        else:
            self.speed(0)
            self.setheading(540 - self.heading())
            self.current_speed *= 1.2
            self.speed(self.current_speed)

    def reset_position(self):
        self.speed(0)
        self.goto(0, 0)
        self.current_speed = 0.91
        self.paddle_bounce()
        self.speed(self.current_speed)
