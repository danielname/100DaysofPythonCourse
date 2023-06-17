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
state_list = states_data["state"].to_list()

state_guess = screen.textinput("Guess a state", "Name another state: ").title()

game = True
while game:
    if state_guess == "Exit":
        break
    if state_guess in state_list:
        pen.x = states_data[states_data.state == state_guess]["x"].max()
        pen.y = states_data[states_data.state == state_guess]["y"].max()
        pen.write_state(state_guess)
        state_guess = screen.textinput("Guess a state", "Name another state: ").title()

    else:
        state_guess = screen.textinput("Guess a state", "Name another state: ").title()


screen.exitonclick()
