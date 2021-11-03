from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def turtle_write(self, text):
        self.clear()
        self.write(text, False, align='center', font=FONT)
