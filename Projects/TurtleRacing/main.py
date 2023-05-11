from turtle import Turtle, Screen
from random import randint

race = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color (red/blue/green/yellow/purple/pink/black): ")
colors = ["red","blue","green","yellow","purple","pink","black"]
racers = []

for index in range(7):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[index])
    turtle.penup()
    turtle.goto(-230, 160 - (index * 50))
    racers.append(turtle)

if user_bet:
    race = True

while race:
    for turtle in racers:
        if race:
            turtle.forward(randint(0,10))
        if turtle.xcor() >= 230:
            race = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"Winner! Your {winner} turtle finished first!")
            else:
                print(f"The {winner} turtle finished first. You lose.")


screen.exitonclick()

