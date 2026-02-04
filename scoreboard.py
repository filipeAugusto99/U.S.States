from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def add_state_screen(self, pos_x, pos_y, name_state):
        self.goto(pos_x, pos_y)
        self.write(arg=f"{name_state}", move=False, align="center", font=("Courier", 14, "normal"))