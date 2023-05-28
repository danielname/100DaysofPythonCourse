from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.ht()
        self.penup()
        self.goto(0, 280)
        self.score = 0
        self.high_score = 0
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", font=("Arial", 12, "normal"), align="center")

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update()


