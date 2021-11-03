from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.level = 1
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)
        self.reset_player()

    def reset_player(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            self.level += 1
