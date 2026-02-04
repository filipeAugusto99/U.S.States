import turtle
from scoreboard import Scoreboard


scoreboard = Scoreboard()
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# Use a loop to allow the user to keep guessing
while len(scoreboard.correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(scoreboard.correct_guesses)}/50 Guess the States",
                                    prompt="What's another state's name?")
    titled_answer = answer_state.title()

    if titled_answer not in scoreboard.correct_guesses:
        # Check if the guess is among the 50 states
        if titled_answer in scoreboard.states_list:
            # Write correct guesses onto the map
            scoreboard.add_state_screen(titled_answer)
screen.exitonclick()