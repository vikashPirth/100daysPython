from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 260)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 260)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)

    def left_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def right_score(self):
        self.r_score += 1
        self.update_scoreboard()
