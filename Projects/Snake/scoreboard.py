from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.ht()
        self.penup()
        self.goto(-50, 280)
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}", font=("Arial", 12, "normal"))
