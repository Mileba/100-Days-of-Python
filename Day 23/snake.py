from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        """Create a snake class"""
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        """Create the snake body"""
        for number in range(3):
            position = number * -20
            self.add_body(position)

    def add_body(self, position):
        """Add a new part to the snake body"""
        tim = Turtle('square')
        tim.color('white')
        tim.penup()
        tim.setposition(position, 0)
        self.snake_body.append(tim)

    def reset_snake(self):
        for body in self.snake_body:
            body.goto(900,900)

        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]


    def extend(self):
        self.add_body(1)

    def move(self):
        """Moves the snake forward"""
        for body in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[body - 1].xcor()
            new_y = self.snake_body[body - 1].ycor()
            self.snake_body[body].goto(new_x, new_y)

        self.head.forward(20)

    def up(self):
        """Moves the snake up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Moves the snake down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        """Moves the snake right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        """Moves the snake left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
