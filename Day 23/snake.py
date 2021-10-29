from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        for number in range(3):
            position = number * -20
            tim = Turtle('square')
            tim.color('white')
            tim.penup()
            tim.setposition(position, 0)
            self.snake_body.append(tim)

    def move(self):
        for body in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[body - 1].xcor()
            new_y = self.snake_body[body - 1].ycor()
            self.snake_body[body].goto(new_x, new_y)

        self.snake_body[0].forward(20)