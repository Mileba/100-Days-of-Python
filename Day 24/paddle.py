from turtle import Turtle

UP = 90
DOWN = 270


class Paddle(Turtle):
    """Create the Paddle, it takes 2 input. The x position and y position"""
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.speed(0)
        self.penup()
        self.setheading(UP)
        self.shape("square")
        self.color("white")
        self.shapesize(1, 4)
        self.setpos(x_pos, y_pos)

    def up_button(self):
        """Creates a event listener that moves the paddle up"""
        self.setheading(UP)
        self.forward(15)

    def down_button(self):
        """Creates a event listener that moves the paddle down"""
        self.setheading(DOWN)
        self.forward(15)
