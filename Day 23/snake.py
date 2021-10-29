from turtle import Turtle


class Snake:
    def __init__(self):
        pass

    def snake_body(self):
        snake_body = []

        for number in range(3):
            position = number * -20
            tim = Turtle('square')
            tim.color('white')
            tim.penup()
            tim.setposition(position, 0)
            snake_body.append(tim)
