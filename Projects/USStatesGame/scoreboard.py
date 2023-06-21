from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.penup()
        self.goto(0, 250)
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}/50", font=("Arial", 12, "normal"), align="center")

