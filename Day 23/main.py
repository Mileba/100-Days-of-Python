from turtle import Screen, Turtle

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")

for number in range(3):
    position = number * -21
    tim = Turtle('square')
    tim.color('white')
    tim.setposition(position, 0)

screen.exitonclick()
