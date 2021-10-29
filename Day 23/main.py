from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()


snake = Snake().snake_body()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for body in range(len(snake) - 1, 0, -1):
        new_x = snake[body - 1].xcor()
        new_y = snake[body - 1].ycor()
        snake[body].goto(new_x, new_y)

    snake[0].forward(20)
#
screen.exitonclick()
