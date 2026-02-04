from turtle import Turtle
import pandas


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.states_data = pandas.read_csv("50_states.csv")
        self.states_list = self.states_data["state"].to_list()
        self.correct_guesses = set()


    def add_state_screen(self, name_state):
        state_pos = self.states_data[self.states_data.state == name_state]
        state_pos_x = state_pos.x.iloc[0]
        state_pos_y = state_pos.y.iloc[0]
        self.goto(state_pos_x, state_pos_y)
        self.write(arg=f"{name_state}",
                   move=False,
                   align="center",
                   font=("Courier", 11, "normal"))
        self.correct_guesses.append(name_state)