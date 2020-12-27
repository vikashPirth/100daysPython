from turtle import Turtle
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-270, 270)
        self.scoreboard()

    def scoreboard(self):
        self.write(f"Level:  {self.level}", align="left", font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.level +=1
        self.write(f"Level:  {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align="center", font=FONT)
