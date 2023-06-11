import turtle
import writer
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

pen = writer.Writer()


states_data = pandas.read_csv("50_states.csv")

state_guess = screen.textinput("Guess a state", "Name another state: ").title()

game = True
while game:

    if states_data[states_data.state == state_guess].index > -1: #something is wrong with this. If i make an error it bugs out.
        pen.x = states_data[states_data.state == state_guess]["x"].max()
        pen.y = states_data[states_data.state == state_guess]["y"].max()
        pen.write_state(state_guess)
        state_guess = screen.textinput("Guess a state", "Name another state: ").title()

    else:
        state_guess = screen.textinput("Guess a state", "Name another state: ")


screen.exitonclick()
