from turtle import Turtle, Screen
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

screen = Screen()

screen.setup(500, 400)

racers = []

for number in range(len(colors)):
    angle = number * 20
    position = angle + -100
    tim = Turtle('turtle')
    tim.color(colors[number])
    tim.penup()
    tim.goto(-240, position)
    racers.append(tim)

print(racers)

user_bet = screen.textinput('Make your bet', 'Which colour would win the race')


state = False
winner = ''

while not state:
    for racer in racers:
        if racer.xcor() > 210:
            winner = racer.color()[0]
            state = True
        else:
            racer.forward(random.randrange(0, 10))

if user_bet == winner:
    print(f"You Win, The winning turtle is color {winner}")
else:
    print(f"You lose, The winning Turtle is color {winner}")





screen.exitonclick()
