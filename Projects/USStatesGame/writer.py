from turtle import Turtle

FONT = ("Courier", 12, "normal")

class Writer (Turtle):

    def __init__(self):
        super().__init__(visible=False)
        x = 0
        y = 0
        self.speed(0)
        self.penup()

    def write_state(self, state):
        self.goto(self.x, self.y)
        self.write(state, align="center", font=FONT)
