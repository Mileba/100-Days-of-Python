from turtle import Turtle

RIGHT = 0
LEFT = 180


class Ball(Turtle):
    """Create the ball class"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("fast")
        self.penup()
        self.setheading(LEFT)
        self.goto(240, 0)

    def move(self):
        """move the ball forward"""
        self.forward(3)
