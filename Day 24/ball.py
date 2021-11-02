from turtle import Turtle

RIGHT = 0
LEFT = 180


class Ball(Turtle):
    """Create the ball class"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        # self.speed("slowest")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        """move the ball forward"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        """Bounce the ball when it hits the wall"""
        self.y_move *= -1

    def paddle(self):
        self.x_move *= -1


