from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake_body = []

for number in range(3):
    position = number * -20
    tim = Turtle('square')
    tim.color('white')
    tim.penup()
    tim.setposition(position, 0)
    snake_body.append(tim)
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for body in range(len(snake_body) - 1, 0, -1):
        new_x = snake_body[body - 1].xcor()
        new_y = snake_body[body - 1].ycor()
        snake_body[body].goto(new_x, new_y)

    snake_body[0].forward(20)

screen.exitonclick()
