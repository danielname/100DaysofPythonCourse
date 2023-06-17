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
hit_list = []
state_guess = screen.textinput("Guess a state", "Name another state: ").title()

game = True
while game:
    if state_guess == "Exit":
        data_dict = {"state": state_list}
        study = pandas.DataFrame(data_dict)
        study.to_csv("state_study_list.csv")
        break
    if state_guess in state_list:
        pen.x = states_data[states_data.state == state_guess]["x"].max()
        pen.y = states_data[states_data.state == state_guess]["y"].max()
        pen.write_state(state_guess)
        state_list.pop(state_list.index(state_guess))
        state_guess = screen.textinput("Guess a state", "Name another state: ").title()
    else:
        state_guess = screen.textinput("Guess a state", "Name another state: ").title()


screen.exitonclick()

#make a hint button/command that access the remaining states
#count that shows how many are correct
