from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard (Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.speed(0)
        self.penup()
        self.goto(-200,250)
        self.level = 0
        self.level_up()

    def level_up(self):
        self.level += 1
        self.clear()
        self.write("Level: " + str(self.level),  align="center", font=FONT)
