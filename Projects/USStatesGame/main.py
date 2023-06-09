import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")

state_guess = screen.textinput("Guess a state", "Name another state: ")

x = 0
y = 0

# if state_guess in states_data.state:

