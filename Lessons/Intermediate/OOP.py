# #basic way to import a class
# import turtle
# # name = module.Class()
# new_turtle = turtle.Turtle()

# shorter
from turtle import Turtle, Screen
new_turtle = Turtle()
new_turtle.shape('turtle')
new_turtle.color('chartreuse4')
new_turtle.forward(100.00)

my_screen = Screen()
print(my_screen.canvheight)

my_screen.exitonclick()

# imported package:
# view | tool windows | python Packages
# Search
# import
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)