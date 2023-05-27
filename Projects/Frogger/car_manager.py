from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager:

    def __init__(self):
        self.cars = []
        self.driving_speed = STARTING_MOVE_DISTANCE
        for car in range(20):
            self.add_car((randint(-250,250), randint(-250,280)))

    def add_car(self, position):
        turtle = Turtle("square")
        turtle.shapesize(stretch_wid=1, stretch_len=2)
        turtle.color(choice(COLORS))
        turtle.penup()
        turtle.setheading(180)
        turtle.goto(position)
        self.cars.append(turtle)

    def drive(self):
        for car in self.cars:
            car.forward(self.driving_speed)
            if car.xcor() < -320:
                car.goto(320, car.ycor())
