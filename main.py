import turtle
from secrets import token_urlsafe
from scoreboard import Scoreboard
import pandas


scoreboard = Scoreboard()
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


states_data = pandas.read_csv("50_states.csv")
states_dict = states_data.to_dict()
states_list = states_data["state"].to_list()


# Record the correct guesses in a list
correct_guesses = []


# Use a loop to allow the user to keep guessing
while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 Guess the States", prompt="What's another state's name?")
    titled_answer = answer_state.title()

    if titled_answer not in correct_guesses:
        # Check if the guess is among the 50 states
        if titled_answer in states_list:
            # Write correct guesses onto the map
            state_pos = states_data[states_data.state == f"{titled_answer}"]
            state_pos_x = state_pos.x.iloc[0]
            state_pos_y = state_pos.y.iloc[0]
            scoreboard.add_state_screen(state_pos_x, state_pos_y, titled_answer)
            correct_guesses.append(titled_answer)

screen.exitonclick()