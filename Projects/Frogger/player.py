from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__("turtle")
        self.penup()
        self.speed(0)
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def hop(self):
        self.fd(MOVE_DISTANCE)

