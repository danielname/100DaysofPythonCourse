from turtle import Turtle
with open("high_score.txt") as HS:
    HIGH_SCORE = int(HS.read())


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.ht()
        self.penup()
        self.goto(0, 280)
        self.score = 0
        self.high_score = HIGH_SCORE
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", font=("Arial", 12, "normal"), align="center")

    def game_over(self):
        if self.score > self.high_score:
            with open("high_score.txt", mode="w") as HS:
                HS.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.update()


