from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.write(f"{self.score}")
        self.goto(x_pos, y_pos)
