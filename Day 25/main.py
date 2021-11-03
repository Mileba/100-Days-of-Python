import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()
game_over = Scoreboard()
score.goto(-230, 250)
# game_over.goto(0, 0)

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    score.turtle_write(f"Level:{player.level}")

    car_manager.create_car()
    car_manager.move()

    if player.level > 1:
        car_manager.increase_speed()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_over.turtle_write("Game over")
            game_is_on = False

screen.exitonclick()
