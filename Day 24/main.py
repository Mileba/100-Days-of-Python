from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

screen = Screen()

screen.screensize(500, 500)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.listen()
line = Turtle()
line.speed(0)
line.width(3)
line.color("white")
line.penup()
line.goto(0, -250)
line.setheading(90)
line.hideturtle()

for _ in range(35):
    line.pendown()
    line.forward(10)
    line.penup()
    line.forward(5)

left_paddle = Paddle(270, 0)
right_paddle = Paddle(-270, 0)
screen.onkey(left_paddle.up_button, "Up")
screen.onkey(left_paddle.down_button, "Down")
screen.onkey(right_paddle.up_button, "w")
screen.onkey(right_paddle.down_button, "s")
ball = Ball()

game_is_on = True

while game_is_on:
    ball.move()

screen.exitonclick()
