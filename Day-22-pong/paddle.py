from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)
        self.color("white")

    def move_up(self):
        self.penup()
        new_y = self.ycor() + 60
        self.goto(self.xcor(), new_y)

    def move_down(self):
        self.penup()
        new_y = self.ycor() - 60
        self.goto(self.xcor(), new_y)
