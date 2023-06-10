import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

writer = turtle.Turtle(visible=False)
writer.speed(0)
writer.penup()

states_data = pandas.read_csv("50_states.csv")

state_guess = screen.textinput("Guess a state", "Name another state: ")

x = 0
y = 0

if state_guess in states_data.state:
    x = states_data.state.state_guess.x
    y = states_data.state.state_guess.y
    writer.goto(x,y)
    writer.write(state_guess, align="center")

screen.exitonclick()