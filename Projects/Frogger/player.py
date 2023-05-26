from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__("turtle")
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.starting_line()

    def hop(self):
        self.fd(MOVE_DISTANCE)

    def starting_line(self):
        self.goto(STARTING_POSITION)

