import random
import turtle
import writer
import pandas
import scoreboard

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

pen = writer.Writer()
score = scoreboard.ScoreBoard()

states_data = pandas.read_csv("50_states.csv")
state_list = states_data["state"].to_list()
hit_list = []
state_guess = screen.textinput("Guess a state", "Name another state: ").title()

game = True
hints_remaining = 2
while game:
    if state_guess == "Exit":
        data_dict = {"state": state_list}
        study = pandas.DataFrame(data_dict)
        study.to_csv("state_study_list.csv")
        break
    if state_guess == "Hint":
        if hints_remaining > 0:
            hints_remaining -= 1
            hint = random.choice(state_list)[0]
            state_guess = screen.textinput("Guess a state", f"Starts with a(n): {hint}").title()
        else:
            state_guess = screen.textinput("No Hints Left", "Name another state: ").title()
    if state_guess in state_list:
        pen.x = states_data[states_data.state == state_guess]["x"].max()
        pen.y = states_data[states_data.state == state_guess]["y"].max()
        pen.write_state(state_guess)
        score.score += 1
        score.update()
        state_list.pop(state_list.index(state_guess))
        state_guess = screen.textinput("Guess a state", "Name another state: ").title()
    else:
        state_guess = screen.textinput("Guess a state", "Name another state: ").title()


screen.exitonclick()

#count that shows how many are correct
