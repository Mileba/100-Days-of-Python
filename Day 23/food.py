from turtle import Turtle
import random


class Food(Turtle):
    """Creates a Food for the snake"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed(0)
        self.refresh()

    def refresh(self):
        """Generate the food at random location"""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
