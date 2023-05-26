from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager:

    def __init__(self):
        self.cars = []
        for car in range(20):
            self.add_car((randint(-250,250), randint(-250,280)))

    def add_car(self, position):
        turtle = Turtle("square")
        turtle.color(choice(COLORS))
        turtle.penup()
        turtle.goto(position)
        self.cars.append(turtle)
