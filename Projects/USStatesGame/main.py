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

state_guess = screen.textinput("Guess a state", "Name another state: ")



if state_guess in states_data.state:
    pen.x = states_data.state.state_guess.x
    pen.y = states_data.state.state_guess.y


screen.exitonclick()
