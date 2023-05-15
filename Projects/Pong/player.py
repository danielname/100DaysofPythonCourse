from turtle import Turtle

MOVE_DISTANCE = 28


class Player(Turtle):

    def __init__(self, location):
        super().__init__("square")
        self.speed(0)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(location)

    def move_up(self):
        self.sety(self.ycor() + MOVE_DISTANCE)

    def move_down(self):
        self.sety(self.ycor() - MOVE_DISTANCE)
