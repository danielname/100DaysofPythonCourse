import turtle
import writer
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

writer = turtle.Turtle(visible=False)


states_data = pandas.read_csv("50_states.csv")

state_guess = screen.textinput("Guess a state", "Name another state: ")



if state_guess in states_data.state:
    x = states_data.state.state_guess.x
    y = states_data.state.state_guess.y


screen.exitonclick()