from turtle import Screen
import time
from random import randint

from player import Player
from cars import Cars
from scoreboard import Score


def spawn_car():
    if randint(1, 6) == 1:
        return True
    return False


screen = Screen()
screen.setup(600, 600)
screen.title("Turtle Road")
screen.tracer(0)

player = Player()
cars = Cars()
score = Score()

screen.onkeypress(player.move, "space")
screen.listen()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Spawn moving car at random times
    if spawn_car():
        cars.create_car()

    cars.move()

    for car in cars.cars:
        # Detect collision
        if player.distance(car) < 20:
            game_is_on = False
            score.game_over()

    # Detect if reached top
    if player.ycor() > 280:
        cars.restart()
        cars.update_speed()
        player.set_start()
        score.update_level()


screen.exitonclick()
