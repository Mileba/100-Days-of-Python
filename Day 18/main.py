from turtle import *

tim = Turtle()
tim.shape("turtle")
tim.color("red")

for _ in range(20):
    tim.forward(4)
    tim.penup()
    tim.forward(4)
    tim.pendown()

screen = Screen()

